import asyncio
from openrouter import llm_call
from inputs import PROMPTS_CONFIG
from utils import get_result_word, save_response_to_csv


async def test_prompt(
        prompt_number: str, llm_model: str, testcases: list[tuple[str, str]]
) -> tuple[str, str]:

    expected_results = []
    llm_ainvokes = []

    prompt_config = PROMPTS_CONFIG.get(prompt_number)
    for index, specification, expected_result in testcases:
        llm_invoke = llm_call(
            llm_model=llm_model,
            input_text=specification,
            index_of_testcase=index,
            **prompt_config
        )
        llm_ainvokes.append(llm_invoke)
        expected_results.append(expected_result)

    llm_results = await asyncio.gather(*llm_ainvokes)

    testcase_results = list(zip(llm_results, expected_results))

    short_result = ""
    long_result = ""
    result_testing_tuples = []

    for index, testcase in enumerate(testcase_results):
        result_from_llm = testcase[0]
        expected_result = testcase[1]
        long_result += f"-\n"
        long_result += f"\t\t\tTESTCASE-{index + 1}:\n"
        for sentence in str(result_from_llm).split("\n"):
            if "RESULT" in sentence:
                result_testing_tuples.append(
                    (
                        index + 1,
                        expected_result,
                        sentence.replace("RESULT:", "").strip(),
                        result_from_llm,
                        llm_model,
                        prompt_number
                    )
                )
                short_result += f"-\n"
                short_result += f"\t\t\tTESTCASE-{index + 1}: " + expected_result + "\n"
                short_result += f"LLM RESPONSE: " + sentence + "\n\n"
                short_result += "Result: **" + get_result_word(expected_result, sentence) + "**\n\n\n\n"
            long_result += f"{sentence}\n\n"
        long_result += "Expected RESPONSE: **" + expected_result + "**\n\n\n\n"

    save_response_to_csv(result_testing_tuples)
    return short_result, long_result

