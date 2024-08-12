import asyncio
from config import DEFAULT_LLM_MODEL, CSV_FILE_PATH
from constants import (
    OPTIONS,
    INSTRUCTION,
    PROMPT,
    INPUT_TEXT_1,
    INPUT_TEXT_2,
    INPUT_TEXT_3,
    INPUT_TEXT_4,
    INPUT_TEXT_5,
    INPUT_TEXT_6,
    INPUT_TEXT_7,
    INPUT_TEXT_8,
    INPUT_TEXT_9,
)
from openrouter import llm_call
from utils import write_tuples_to_csv, read_csv_to_tuples, similarity_percentage




async def get_test_prompt(
        prompt: str, llm_model: str, temperature: str, options: str, instruction: str
) -> tuple[str, str]:
    if not llm_model:
        llm_model = DEFAULT_LLM_MODEL

    if not temperature:
        temperature = 0

    if not options:
        options = OPTIONS

    if not instruction:
        instruction = INSTRUCTION

    if not prompt:
        prompt = PROMPT

    temperature = float(temperature)

    testcases_list = read_csv_to_tuples(CSV_FILE_PATH)

    testcase_results = []
    expected_results = []

    testcases_ainvokes = []

    for specification, expected_result in testcases_list:
        llm_invoke = llm_call(
            prompt=prompt,
            llm_model=llm_model,
            temperature=temperature,
            options=options,
            instruction=instruction,
            input_text=specification,
        )
        testcases_ainvokes.append(llm_invoke)
        expected_results.append(expected_result)

    llm_results = await asyncio.gather(*testcases_ainvokes)

    for i in range(len(llm_results)):
        testcase_results.append((llm_results[i], expected_results[i]))

    short_result = ""
    long_result = ""

    for index, testcase in enumerate(testcase_results):
        result_llm = testcase[0]
        expected_result = testcase[1]
        long_result += f"-\n"
        long_result += f"\t\t\tTESTCASE-{index + 1}:\n"
        for sentence in str(result_llm).split("\n"):
            if "RESULT" in sentence:
                short_result += f"-\n"
                short_result += f"\t\t\tTESTCASE-{index + 1}:\n"
                short_result += "LLM RESPONSE ㅤㅤ: " + sentence + "\n\n"
                short_result += "Expected RESPONSE: **" + expected_result + "**\n\n\n\n"
                short_result += (
                        "Accuracy: "
                        + str(similarity_percentage(sentence, expected_result))
                        + "\n\n\n\n"
                )
            long_result += f"{sentence}\n\n"
        long_result += "Expected RESPONSE: **" + expected_result + "**\n\n\n\n"

    return short_result, long_result


if __name__ == "__main__":
    # Script for writing inputs to csv:
    tuples_list = [
        (INPUT_TEXT_1, "RESULT: 1200-N - 3mm HPL Frts & HPL Ends NAUF PB Core"),
        (
            INPUT_TEXT_2,
            "RESULT: 1100-C - Sq Flat Edge HPL Frts & HPL Ends IPB CARB Compliant Core",
        ),
        (INPUT_TEXT_3, "RESULT: 2800 Series"),
        (INPUT_TEXT_4, "RESULT: 1200 Series"),
        (INPUT_TEXT_5, "RESULT: 1200 Series"),
        (INPUT_TEXT_6, "RESULT: 3200 Series"),
        (INPUT_TEXT_7, "RESULT: 2200 Series"),
        (INPUT_TEXT_8, "RESULT: 1250 Series"),
        (INPUT_TEXT_9, "RESULT: 2100-C"),
    ]
    csv_file_path = "../testcases.csv"
    write_tuples_to_csv(csv_file_path, tuples_list)
    print(f"Data written to {csv_file_path}")

    # count = 1
    # for i, r in tuples_list:
    #     index = i.find('\xb3')
    #     if index != -1:
    #         print(f"Символ знайдено на позиції {index} в  INPUT-{count}.")
    #         print(i[index])
    #         print(i[index])
    #         print(i[index:index+100])
    #     count += 1
