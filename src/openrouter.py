from src.config import client


async def llm_call(
        prompt: str, llm_model: str, temperature: float, options: str, instruction: str, input_text: str
):
    completion = await client.chat.completions.create(
        model=llm_model,
        temperature=temperature,
        messages=[
            {
                "role": "assistant",
                "content": prompt.format(
                    OPTIONS=options, INSTRUCTION=instruction, INPUT_TEXT=input_text
                ),
            },
        ],
    )
    return completion.choices[0].message.content
