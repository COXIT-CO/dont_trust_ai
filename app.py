import streamlit as st

from main import get_test_prompt

st.set_page_config(page_title="Prompt test", layout="wide")

st.title("Prompt test")
st.header("Test your prompt")

with st.form("my_form"):
    input_llm = st.text_input("Input LLM model: ", key="input_llm", value="anthropic/claude-3.5-sonnet")
    input_temp = st.text_input("Input temperature of model: ", key="input_temp", value="0")

    input_prompt = st.text_input("Input your prompt: ", key="input_prompt")

    submitted = st.form_submit_button("Let's test")

    if submitted:

        response = get_test_prompt(input_prompt, input_llm, input_temp)
        st.subheader("Result: ")
        st.write(response)
