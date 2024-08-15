from config import client, logging


async def llm_call(
        prompt_template: str,
        llm_model: str,
        options: str,
        instruction: str,
        input_text: str,
        index_of_testcase: int
):
    logging.info(f"🟡------------TESTCASE-{index_of_testcase}------------🟡\n")
    logging.info(f"✅------------Send request to {llm_model}------------✅\n")
    logging.info(f"Prompt template: 👉 {prompt_template}\n\n")
    logging.info(f"Instruction: 👉 {instruction}\n\n")
    logging.info(f"Specification: 👉 {input_text[:600]}\n\n")
    try:
        completion = await client.chat.completions.create(
            model=llm_model,
            temperature=0,
            messages=[
                {
                    "role": "system",
                    "content": prompt_template.format(
                        OPTIONS=options, INSTRUCTION=instruction, INPUT_TEXT=input_text
                    ),
                },
            ],
        )
    except Exception as e:
        logging.exception(e)
        return f":red[Caught an ERROR: {e}]"

    llm_response = completion.choices[0].message.content
    logging.info(f"TESTCASE-{index_of_testcase} -> Received LLM response: ☎️\n {llm_response}\n\n\n\n")
    return llm_response
