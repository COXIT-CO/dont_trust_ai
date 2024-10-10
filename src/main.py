import asyncio
import pandas as pd
from pandas import DataFrame

from csv_utils import save_response_to_csv
from streamlit_tools import get_result_word
from config import CSV_HEADERS_PROMPT_TESTING, CSV_HEADERS_DEEPEVAL_TESTING
from llm_calls import (
    call_llm_with_langsmith_monitoring,
    call_llm_with_deepeval_monitoring,
)


async def test_prompt(
    prompt_number: int,
    prompt_template: str,
    prompt_instruction: str,
    prompt_options: str,
    llm_model: str,
    testcases: list[tuple[str, str, str]],
) -> tuple[str, str, int]:
    """
        Tests a prompt against multiple test cases using the specified LLM model and saves the results.

        Args:
            prompt_number (int): The index of the prompt being tested.
            prompt_template (str): The template of the prompt.
            prompt_instruction (str): Instructions for the prompt.
            prompt_options (str): Options for the prompt.
            llm_model (str): The LLM model to be used for testing.
            testcases (list[tuple[str, str]]): A list of tuples where each tuple contains:
                - Index of the testcase.
                - The expected result.
                - The input specification for the LLM.
        Returns:
            tuple[str, str, int]: A tuple containing:
                - Short result summary as a string.
                - Detailed result summary as a string.
                - Number of test cases that passed.
        """

    expected_results = []
    llm_ainvokes = []
    for index, expected_result, specification in testcases:
        llm_invoke = call_llm_with_langsmith_monitoring(
            llm_model=llm_model,
            index_of_testcase=index,
            prompt_template=prompt_template,
            instruction=prompt_instruction,
            options=prompt_options,
            input_text=specification,
        )
        llm_ainvokes.append(llm_invoke)
        expected_results.append(expected_result)

    llm_results = await asyncio.gather(*llm_ainvokes)

    testcase_results = list(zip(llm_results, expected_results))

    short_result = ""
    long_result = ""
    result_testing_tuples = []
    passed_testcases = 0

    for testcase in testcase_results:
        index, result_from_llm, _, _, _ = testcase[0]
        expected_result = testcase[1]
        long_result += f"-\n"
        long_result += f"\t\t\tTESTCASE-{index}:\n"
        for sentence in str(result_from_llm).split("\n"):
            if "RESULT" in sentence:
                result_testing_tuples.append(
                    (
                        index,
                        expected_result,
                        sentence.replace("RESULT:", "").strip(),
                        result_from_llm,
                        prompt_template,
                        prompt_instruction,
                        prompt_options,
                        llm_model,
                        prompt_number,
                    )
                )
                state_of_result = get_result_word(expected_result, sentence)
                if state_of_result == ":green[success]":
                    passed_testcases += 1
                short_result += f"-\n"
                short_result += f"\t\t\tTESTCASE-{index}: " + expected_result + "\n"
                short_result += f"LLM RESPONSE: " + sentence + "\n\n"
                short_result += "Result: **" + state_of_result + "**\n\n\n\n"

            long_result += f"{sentence}\n\n"
        long_result += "Expected RESPONSE: **" + expected_result + "**\n\n\n\n"
    save_response_to_csv(data=result_testing_tuples, columns=CSV_HEADERS_PROMPT_TESTING)
    return short_result, long_result, passed_testcases


async def get_df_results_of_testing(
    prompt_template: str,
    prompt_instruction: str,
    prompt_options: str,
    llm_model: str,
    testcases: list[tuple[str, str, str]],
) -> DataFrame:
    """
        Call LLM's testing using DeepEval monitoring and return the LLM's responses  in a DataFrame.

        Args:
            prompt_template (str): The template of the prompt to be used.
            prompt_instruction (str): Instructions for the prompt.
            prompt_options (str): Options for the prompt.
            llm_model (str): The LLM model to be used for testing.
            testcases (list[tuple[str, str, str]]): A list of tuples where each tuple contains:
                - Index of the testcase.
                - The expected result.
                - The input specification for the LLM.
        Returns:
            DataFrame: A DataFrame containing the LLM's responses along with the input specifications,
                       expected results, and additional test information.
    """

    expected_results = []
    specifications = []
    llm_ainvokes = []
    for index, expected_result, specification in testcases:
        llm_invoke = call_llm_with_deepeval_monitoring(
            llm_model=llm_model,
            index_of_testcase=index,
            prompt_template=prompt_template,
            instruction=prompt_instruction,
            options=prompt_options,
            input_text=specification,
        )
        llm_ainvokes.append(llm_invoke)
        expected_results.append(expected_result)
        specifications.append(specification)

    llm_results = await asyncio.gather(*llm_ainvokes)

    testcase_results = list(zip(llm_results, expected_results, specifications))

    result_testing_tuples = []

    for testcase in testcase_results:
        index, result_from_llm, completion_time, total_cost, response_id = testcase[0]
        expected_result = testcase[1]
        specification = testcase[2]
        prompt = (
            prompt_template.format(
                OPTIONS=prompt_options, INSTRUCTION=prompt_instruction
            ),
        )
        result_testing_tuples.append(
            (
                index,
                prompt,
                specification,
                expected_result,
                result_from_llm,
                llm_model,
                response_id,
            )
        )

    save_response_to_csv(
        data=result_testing_tuples,
        columns=CSV_HEADERS_DEEPEVAL_TESTING,
        file_path="deepeval_results",
    )

    return pd.DataFrame(
        data=result_testing_tuples, columns=CSV_HEADERS_DEEPEVAL_TESTING
    )
