import csv
import os
import unittest
import pytz
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


GPT_ACCURACY = 0.7
CLAUDE_ACCURACY = 0.8
RETRY_COUNT = 2

OPENROUTER_BASE_URL = os.environ["OPENROUTER_BASE_URL"]
OPENROUTER_API_KEY = os.environ["OPENROUTER_API_KEY"]
OPTIONS = os.environ["OPTIONS"]


class PromptTests(unittest.TestCase):
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

    def setUpClass(self):
        self.claude_llm = "anthropic/claude-3.5-sonnet-2024-06-20"
        self.gpt_llm = "openai/gpt-4o-2024-05-13"
        self.testcases = self.read_testcases_from_csv("tests/testcases.csv")
        self.gpt_prompt_template = os.environ["GPT_PROMPT"]
        self.claude_prompt_template = os.environ["CLAUDE_PROMPT"]
        self.gpt_instructions = os.environ["INSTRUCTIONS_GPT"]
        self.claude_instructions = os.environ["CLAUDE_INSTRUCTIONS"]

    def test_gpt_prompt(self):
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
                        model=self.gpt_llm,
                        temperature=0,
                        seed=111,
                        messages=[
                            {
                                "role": "system",
                                "content": self.gpt_prompt_template.format(
                                    OPTIONS=OPTIONS,
                                    INSTRUCTION=self.gpt_instructions,
                                    INPUT_TEXT=specification,
                                ),
                            },
                        ],
                    )
                    llm_response = completion.choices[0].message.content

                    for sentence in str(llm_response).split("\n"):
                        if "RESULT" in sentence:
                            if expected_result in sentence:
                                match_count += 1
                                print(
                                    f"Circle-{index_of_circle + 1} "
                                    f"GPT: Test-{index_of_testcase} PASSED"
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
                                    f"GPT: Test-{index_of_testcase} FAILED: "
                                    f"Result: {sentence}"
                                )
                            result_testing_tuples.append(
                                (
                                    index_of_circle,
                                    index_of_testcase,
                                    sentence,
                                    llm_response,
                                    self.gpt_prompt_template,
                                    self.gpt_instructions,
                                    OPTIONS,
                                    self.gpt_llm,
                                )
                            )

        self.save_response_to_csv(
            result_testing_tuples, self.gpt_llm
        )  # Save prompts and llm responses to csv file

        precision_percentage = round(match_count / len(self.testcases) * RETRY_COUNT, 2)
        print(f"Precision percentage is {precision_percentage}")

        self.assertGreaterEqual(
            precision_percentage,
            GPT_ACCURACY,
            f"The match occurred only {match_count} "
            f"times out of {len(self.testcases) * RETRY_COUNT} \n{failed_testcases}",
        )

    def test_claude_prompt(self):
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
                        model=self.claude_llm,
                        temperature=0,
                        seed=9999,
                        messages=[
                            {
                                "role": "system",
                                "content": self.claude_prompt_template.format(
                                    OPTIONS=OPTIONS,
                                    INSTRUCTION=self.claude_instructions,
                                ),
                            },
                            {
                                "role": "user",
                                "content": specification,
                            },
                        ],
                    )

                    llm_response = completion.choices[0].message.content

                    for sentence in str(llm_response).split("\n"):
                        if "RESULT" in sentence:
                            if expected_result in sentence:
                                match_count += 1
                                print(
                                    f"Circle-{index_of_circle + 1} "
                                    f"Claude: Test-{index_of_testcase} PASSED"
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
                                    f"Claude: Test-{index_of_testcase} FAILED: "
                                    f"Result: {sentence}"
                                )
                                result_testing_tuples.append(
                                    (
                                        index_of_circle,
                                        index_of_testcase,
                                        sentence,
                                        llm_response,
                                        self.claude_prompt_template,
                                        self.claude_instructions,
                                        OPTIONS,
                                        self.claude_llm,
                                    )
                                )

        self.save_response_to_csv(
            result_testing_tuples, self.claude_llm
        )  # Save prompts and llm responses to csv file

        precision_percentage = round(match_count / len(self.testcases) * RETRY_COUNT, 2)
        print(f"Precision percentage is {precision_percentage}")

        self.assertGreaterEqual(
            precision_percentage,
            CLAUDE_ACCURACY,
            f"The match occurred only {match_count} "
            f"times out of {len(self.testcases) * RETRY_COUNT} \n{failed_testcases}",
        )


if __name__ == "__main__":
    unittest.main()
