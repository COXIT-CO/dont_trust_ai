import csv
import os
import unittest
import pytz
import json
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.environ["OPENROUTER_API_KEY"]


def load_config(file_path):
    with open(file_path, "r") as file:
        config = json.load(file)

    return config


# Getting parameters for testing
CONFIG_DATA = load_config("tests/config.json")

RETRY_COUNT = CONFIG_DATA.get("RETRY_COUNT", 1)
OPENROUTER_BASE_URL = CONFIG_DATA.get("OPENROUTER_BASE_URL", "")
OPTIONS = CONFIG_DATA.get("OPTIONS", "")
INSTRUCTION = CONFIG_DATA.get("INSTRUCTION", "")

MODELS_CONFIG = [
    {
        "name": "GPT",
        "model": CONFIG_DATA.get("GPT_MODEL", ""),
        "accuracy": CONFIG_DATA.get("GPT_ACCURACY", 0.7),
        "prompt_template": CONFIG_DATA.get("GPT_PROMPT_TEMPLATE", ""),
    },
    {
        "name": "CLAUDE",
        "model": CONFIG_DATA.get("CLAUDE_MODEL", ""),
        "accuracy": CONFIG_DATA.get("CLAUDE_ACCURACY", 0.8),
        "prompt_template": CONFIG_DATA.get("CLAUDE_PROMPT_TEMPLATE", ""),
    },
    {
        "name": "QWEN",
        "model": CONFIG_DATA.get("QWEN_MODEL", ""),
        "accuracy": CONFIG_DATA.get("QWEN_ACCURACY", 0.65),
        "prompt_template": CONFIG_DATA.get("QWEN_PROMPT_TEMPLATE", ""),
    },
]


class PromptTests(unittest.TestCase):
    @staticmethod
    def accuracy_counter(match_count: int, testcases: list) -> float:
        accuracy = round(match_count / (len(testcases) * RETRY_COUNT), 2)
        print(f"Accuracy is {accuracy}")
        return accuracy

    @staticmethod
    def read_testcases_from_csv(file_path: str) -> list:
        """
        Reads a CSV file and returns a list of tuples (index, label, specification).

        Args:
            file_path (str): Path to the CSV file with test cases.

        Returns:
            list: List of tuples (index, label, specification).
        """
        result = []

        try:
            with open(file_path, "r") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    index, label, specification = row
                    result.append((index.strip(), label.strip(), specification.strip()))
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found in path: {file_path}")
        return result[1:]

    @staticmethod
    def save_response_to_csv(data: list[tuple], llm_name: str) -> None:
        """
        Writes a list of tuples to a CSV file.

        Args:
            data (list): List of tuples (
                (
                "Circle Number",
                "Test Number",
                "Expected Label",
                "LLM Result",
                "LLM Step by Step Reasoning",
                "Prompt Template",
                "INSTRUCTION",
                "OPTIONS",
                "LLM"
                )
            )
            llm_name (str): name of LLM
        """

        now = datetime.now(pytz.timezone("Europe/Kiev")).strftime("%Y-%m-%d-%H-%M-%S")

        with open(f"tests_results/{llm_name}-{now}.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(
                [
                    "Circle Number",
                    "Test Number",
                    "Expected Label",
                    "LLM Result",
                    "LLM Step by Step Reasoning",
                    "Prompt Template",
                    "INSTRUCTION",
                    "OPTIONS",
                    "LLM",
                ]
            )
            for row in data:
                writer.writerow(row)

    def setUp(self):
        self.testcases = self.read_testcases_from_csv("tests/testcases.csv")

    def run_model_test(
        self,
        model_name: str,
        model: str,
        prompt_template: str,
        accuracy_threshold: float,
    ):
        match_count = 0
        failed_testcases = ""
        result_testing_tuples = []
        client = OpenAI(
            base_url=OPENROUTER_BASE_URL,
            api_key=OPENROUTER_API_KEY,
        )
        for index_of_circle in range(
            RETRY_COUNT
        ):  # Retry tests for correct evaluation precision
            for index_of_testcase, expected_result, specification in self.testcases:
                with self.subTest(i=index_of_testcase):  # subTest for every llm call
                    completion = client.chat.completions.create(
                        model=model,
                        temperature=0,
                        messages=[
                            {
                                "role": "system",
                                "content": prompt_template.format(
                                    OPTIONS=OPTIONS,
                                    INSTRUCTION=INSTRUCTION,
                                ),
                            },
                            {
                                "role": "user",
                                "content": specification,
                            },
                        ],
                    )

                    llm_response = completion.choices[0].message.content
                    index_of_result_word = llm_response.find("RESULT")
                    is_result_found = False

                    for sentence in str(llm_response).split("\n"):
                        if "RESULT" in sentence:
                            is_result_found = True
                            if expected_result in llm_response[index_of_result_word:]:
                                match_count += 1
                                print(
                                    f"Circle-{index_of_circle + 1} "
                                    f"{model_name}: Test-{index_of_testcase} PASSED"
                                )
                            else:
                                failed_testcases += (
                                    f"\nCircle-{index_of_circle + 1} "
                                    f"Testcase-{index_of_testcase}: "
                                    f"Expected: {expected_result} "
                                    f"LLM: {sentence}\n\n"
                                )
                                print(
                                    f"Circle-{index_of_circle + 1} "
                                    f"{model_name}: Test-{index_of_testcase} FAILED: "
                                    f"Result: {sentence}"
                                )
                            result_testing_tuples.append(
                                (
                                    index_of_circle + 1,
                                    index_of_testcase,
                                    expected_result,
                                    sentence,
                                    llm_response,
                                    prompt_template,
                                    INSTRUCTION,
                                    OPTIONS,
                                    model_name,
                                )
                            )
                    if not is_result_found:
                        failed_testcases += (
                            f"\nCircle-{index_of_circle + 1} "
                            f"Testcase-{index_of_testcase}: "
                            f"Expected: {expected_result} "
                            f"ERROR: RESULT WAS NOT FOUND\n\n"
                        )
                        print(
                            f"Circle-{index_of_circle + 1} "
                            f"{model_name}: Test-{index_of_testcase} FAILED: "
                            "ERROR: RESULT WAS NOT FOUND"
                        )
                        result_testing_tuples.append(
                            (
                                index_of_circle + 1,
                                index_of_testcase,
                                expected_result,
                                "RESULT WAS NOT FOUND",
                                llm_response,
                                prompt_template,
                                INSTRUCTION,
                                OPTIONS,
                                model_name,
                            )
                        )

        self.save_response_to_csv(
            result_testing_tuples, model_name
        )  # Save prompt and llm responses to csv file

        accuracy = self.accuracy_counter(match_count, self.testcases)

        self.assertGreaterEqual(
            accuracy,
            accuracy_threshold,
            f"The match occurred only {match_count} "
            f"times out of {len(self.testcases) * RETRY_COUNT} \n{failed_testcases}",
        )

    def test_models(self):
        for config in MODELS_CONFIG:
            with self.subTest(model=config["name"]):
                self.run_model_test(
                    model_name=config["name"],
                    model=config["model"],
                    prompt_template=config["prompt_template"],
                    accuracy_threshold=config["accuracy"],
                )


if __name__ == "__main__":
    unittest.main()
