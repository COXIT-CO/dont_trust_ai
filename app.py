import streamlit as st

from config import DEFAULT_LLM_MODEL
from main import get_test_prompt

st.set_page_config(page_title="Prompt test", layout="wide")

st.title("Prompt test")
st.header("Test your prompt")

with st.form("my_form"):
    input_llm = st.text_input(
        "Input LLM model: ", key="input_llm", value=DEFAULT_LLM_MODEL
    )
    input_temp = st.text_input(
        "Input temperature of model: ", key="input_temp", value="0"
    )

    input_options = st.text_input(
        "Input your options: ", key="input_options"
    )

    input_instruction = st.text_input(
        "Input your instruction: ", key="input_instruction"
    )

    input_prompt = st.text_input(
        "Input your prompt: ", key="input_prompt"
    )

    submitted = st.form_submit_button("Let's test")

    if submitted:
        response = get_test_prompt(
            input_prompt,
            input_llm,
            input_temp,
            input_options,
            input_instruction
        )
        st.subheader("Result: ")
        st.write(response)
