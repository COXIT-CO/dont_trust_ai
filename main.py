from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import dotenv

from dont_trust_ai.constants import (
    OPTIONS,
    INSTRUCTION,
    TEXT,
    INPUT_TEXT_1,
    INPUT_TEXT_2,
    INPUT_TEXT_3
)
from utils import write_tuples_to_csv, read_csv_to_tuples, similarity_percentage

CSV_FILE_PATH = "testcases.csv"

dotenv.load_dotenv()

template = PromptTemplate(
    input_variables=["OPTIONS", "INSTRUCTION", "INPUT_TEXT"],
    template=TEXT
)


def get_llm(model: str, temperature: float):
    return ChatOpenAI(
        temperature=temperature,
        model=model,
        openai_api_base="https://openrouter.ai/api/v1",
    )


def get_test_prompt(prompt: str, llm_model: str, temperature: str) -> dict:
    global template

    if not llm_model:
        llm_model = "anthropic/claude-3.5-sonnet"

    if not temperature:
        temperature = 0

    temperature = float(temperature)

    if prompt:
        template = PromptTemplate(
            input_variables=["OPTIONS", "INSTRUCTION", "INPUT_TEXT"],
            template=prompt
        )

    llm = get_llm(llm_model, temperature)

    chain = template | llm

    testcases_list = read_csv_to_tuples(CSV_FILE_PATH)

    testcases = []

    for specification, expected_result in testcases_list:
        llm_result = chain.invoke(
            input={
                "OPTIONS": OPTIONS,
                "INSTRUCTION": INSTRUCTION,
                "INPUT_TEXT": specification,
            },
        )
        testcases.append((llm_result, expected_result))

    # for specification, _ in testcases_list:
    #     testcases_ainvokes.append(
    #         chain.ainvoke(
    #             input={
    #                 "OPTIONS": OPTIONS,
    #                 "INSTRUCTION": INSTRUCTION,
    #                 "INPUT_TEXT": specification,
    #             },
    #         )
    #     )
    # await asyncio.gather(*testcases_ainvokes)
    #
    # testcases = [(llm_result, testcases_list[index][1]) for index, llm_result in enumerate(testcases_ainvokes)]

    result = ""
    for index, testcase in enumerate(testcases):
        for sentence in str(testcase[0].content).split("\n"):
            if sentence.startswith("RESULT:"):
                result += f"\t\t\t\n"
                result += f"\t\t\tTESTCASE-{index + 1}:\n"
                result += "LLM RESPONSE: " + sentence + "\n\n"
                result += "Expected RESPONSE: " + testcase[1] + "\n\n\n\n"
                result += "Accuracy: " + str(similarity_percentage(sentence, testcase[1])) + "\n\n\n\n"

    return result


if __name__ == '__main__':
    # Example usage:
    tuples_list = [
        (INPUT_TEXT_1, 'RESULT: 1200-N - 3mm HPL Frts & HPL Ends NAUF PB Core'),
        (INPUT_TEXT_2, 'RESULT: 1100-C - Sq Flat Edge HPL Frts & HPL Ends IPB CARB Compliant Core'),
        (INPUT_TEXT_3, 'RESULT: 2800 Series'),
        # (INPUT_TEXT_4, 'RESULT: 1200 Series'),
        # (INPUT_TEXT_5, 'RESULT: 1200 Series'),
        # (INPUT_TEXT_6, 'RESULT: 3200 Series'),
        # (INPUT_TEXT_7, 'RESULT: 2200 Series'),
        # (INPUT_TEXT_8, 'RESULT: 1250 Series'),
        # (INPUT_TEXT_9, 'RESULT: 2100-C'),
    ]
    # count = 1
    # for i, r in tuples_list:
    #     index = i.find('\xb3')
    #     if index != -1:
    #         print(f"Символ знайдено на позиції {index} в  INPUT-{count}.")
    #         print(i[index])
    #         print(i[index])
    #         print(i[index:index+100])
    #     count += 1
    csv_file_path = 'testcases.csv'
    write_tuples_to_csv(csv_file_path, tuples_list)
    print(f"Data written to {csv_file_path}")
