import asyncio
import pandas as pd
from pandas import DataFrame

from openrouter import llm_call
from utils import get_result_word, save_response_to_csv

# Constants
CSV_HEADERS_DEEPEVAL = (
    "Test Number",
    "Prompt",
    "Specification",
    "Expected Result",
    "LLM Response",
    "LLM Model",
)
CSV_HEADERS_TEST = (
    "Test Number",
    "Expected Label",
    "LLM Result",
    "LLM Step by Step Reasoning",
    "Prompt Template",
    "INSTRUCTION",
    "OPTIONS",
    "LLM",
    "Prompt Number",
)


async def test_prompt(
    prompt_number: int,
    prompt_template: str,
    prompt_instruction: str,
    prompt_options: str,
    llm_model: str,
    testcases: list[tuple[str, str]]
) -> tuple[str, str, int]:
    expected_results = []
    llm_ainvokes = []
    for index, expected_result, specification in testcases:
        llm_invoke = llm_call(
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
        index = testcase[0][0]
        result_from_llm = testcase[0][1]
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
    save_response_to_csv(
        data=result_testing_tuples,
        columns=CSV_HEADERS_TEST
    )
    return short_result, long_result, passed_testcases


async def get_df_results_of_testing(
    prompt_template: str,
    prompt_instruction: str,
    prompt_options: str,
    llm_model: str,
    testcases: list[tuple[str, str, str]],
) -> DataFrame:
    expected_results = []
    specifications = []
    llm_ainvokes = []
    for index, expected_result, specification in testcases:
        llm_invoke = llm_call(
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
        index, result_from_llm = testcase[0]
        expected_result = testcase[1]
        specification = testcase[2]
        prompt = (
            prompt_template.format(
                OPTIONS=prompt_options, INSTRUCTION=prompt_instruction
            ),
        )
        result_testing_tuples.append(
            (index, prompt, specification, expected_result, result_from_llm, llm_model)
        )

    save_response_to_csv(
        data=result_testing_tuples,
        columns=CSV_HEADERS_DEEPEVAL,
        file_path="deepeval_results",
    )

    return pd.DataFrame(
        data=result_testing_tuples,
        columns=CSV_HEADERS_DEEPEVAL
    )
