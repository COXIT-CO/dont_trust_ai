import csv
import os
import unittest
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


def read_testcases_from_csv(file_path) -> list:
    """
    Reads a CSV file and returns a list of tuples (index, label, specification).

    Args:
        file_path (str): Path to the CSV file.

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


GPT_ACCURACY = 0.7
CLAUDE_ACCURACY = 0.8
RETRY_COUNT = 2

OPENROUTER_BASE_URL = os.environ["OPENROUTER_BASE_URL"]
OPENROUTER_API_KEY = os.environ["OPENROUTER_API_KEY"]
OPTIONS = os.environ["OPTIONS"]
INSTRUCTIONS_GPT = os.environ["INSTRUCTIONS_GPT"]
CLAUDE_INSTRUCTIONS = os.environ["CLAUDE_INSTRUCTIONS"]


class PromptTests(unittest.TestCase):

    def setUp(self):
        self.claude_llm = "anthropic/claude-3.5-sonnet-2024-06-20"
        self.gpt_llm = "openai/gpt-4o-2024-05-13"
        self.testcases = read_testcases_from_csv("tests/testcases.csv")
        self.gpt_prompt_template = os.environ["GPT_PROMPT"]
        self.claude_prompt_template = os.environ["CLAUDE_PROMPT"]

    def test_gpt_prompt(self):
        match_count = 0
        failed_testcases = ""
        client = OpenAI(
            base_url=OPENROUTER_BASE_URL,
            api_key=OPENROUTER_API_KEY,
        )
        for index_of_circle in range(RETRY_COUNT):
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
                                    INSTRUCTION=INSTRUCTIONS_GPT,
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

        self.assertGreaterEqual(
            round(match_count / len(self.testcases) * RETRY_COUNT, 2),
            GPT_ACCURACY,
            f"The match occurred only {match_count} "
            f"times out of {len(self.testcases) * RETRY_COUNT} \n{failed_testcases}",
        )

    def test_claude_prompt(self):
        match_count = 0
        failed_testcases = ""
        client = OpenAI(
            base_url=OPENROUTER_BASE_URL,
            api_key=OPENROUTER_API_KEY,
        )
        for index_of_circle in range(RETRY_COUNT):
            for index_of_testcase, expected_result, specification in self.testcases:
                with self.subTest(i=index_of_testcase):  # subTest for every llm call
                    completion = client.chat.completions.create(
                        model=self.claude_llm,
                        temperature=0,
                        seed=9999,
                        max_tokens=1000,
                        messages=[
                            {
                                "role": "system",
                                "content": self.claude_prompt_template.format(
                                    OPTIONS=OPTIONS, INSTRUCTION=CLAUDE_INSTRUCTIONS
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

        self.assertGreaterEqual(
            round(match_count / len(self.testcases) * RETRY_COUNT, 2),
            CLAUDE_ACCURACY,
            f"The match occurred only {match_count} "
            f"times out of {len(self.testcases) * RETRY_COUNT} \n{failed_testcases}",
        )


if __name__ == "__main__":
    unittest.main()
