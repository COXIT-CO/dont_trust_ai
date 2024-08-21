import asyncio
from openrouter import llm_call
from utils import get_result_word, save_response_to_csv


async def test_prompt(
    prompt_number: int,
    prompt_template: str,
    prompt_instruction: str,
    prompt_options: str,
    llm_model: str,
    testcases: list[tuple[str, str]]
) -> tuple[str, str]:

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
                        llm_model,
                        prompt_number,
                        prompt_template,
                        prompt_instruction,
                        prompt_options,
                    )
                )
                short_result += f"-\n"
                short_result += f"\t\t\tTESTCASE-{index}: " + expected_result + "\n"
                short_result += f"LLM RESPONSE: " + sentence + "\n\n"
                short_result += (
                    "Result: **"
                    + get_result_word(expected_result, sentence)
                    + "**\n\n\n\n"
                )
            long_result += f"{sentence}\n\n"
        long_result += "Expected RESPONSE: **" + expected_result + "**\n\n\n\n"

    save_response_to_csv(result_testing_tuples)
    return short_result, long_result
