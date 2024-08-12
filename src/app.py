import asyncio

import streamlit as st
from config import DEFAULT_LLM_MODEL, DEFAULT_LLM_TEMPERATURE
from constants import OPTIONS, INSTRUCTION, PROMPT
from main import get_test_prompt


# Function to run the async code within the synchronous Streamlit context


def async_get_test(*args, **kwargs):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop.run_until_complete(get_test_prompt(*args, **kwargs))


# Streamlit app code

def main():
    st.set_page_config(page_title="Prompt test", layout="wide")

    st.title("Prompt test")
    st.header("Test your prompt")

    with st.form("my_form"):
        input_llm = st.text_input(
            "Input LLM model: ", key="input_llm", value=DEFAULT_LLM_MODEL
        )
        input_temp = st.text_input(
            "Input temperature of model: ", key="input_temp", value=DEFAULT_LLM_TEMPERATURE
        )

        input_options = st.text_area("Input your options: ", key="input_options", value=OPTIONS)

        input_instruction = st.text_area(
            "Input your instruction: ", key="input_instruction", value=INSTRUCTION, height=250
        )

        input_prompt = st.text_area("Input your prompt: ", key="input_prompt", value=PROMPT, height=350)

        submitted = st.form_submit_button("Let's test")

        if submitted:
            with st.spinner("Fetching data..."):
                try:
                    short_response, long_response = async_get_test(
                        input_prompt, input_llm, input_temp, input_options, input_instruction
                    )
                except Exception as e:
                    st.error(e)
                    return
            st.subheader("Short Result: ")
            st.write(short_response)
            st.subheader("------------------------------------------------------------")
            st.subheader("Long Result: ")
            st.write(long_response)


if __name__ == "__main__":
    main()
