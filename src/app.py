import asyncio
import streamlit as st

from config import OPENROUTER_DEFAULT_LLM_MODELS
from inputs import PROMPTS_CONFIG, TESTCASES_LIST
from main import test_prompt


def async_get_test(*args, **kwargs):
    """
    Function to run the async code within the synchronous Streamlit context
    """
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop.run_until_complete(test_prompt(*args, **kwargs))


# Streamlit app code

def main():
    st.set_page_config(page_title="Prompt test", layout="wide")

    st.title("Prompt test")
    st.header("Test your prompt")

    with st.form("my_form"):
        selected_llm = st.selectbox('Choose LLM model: ', OPENROUTER_DEFAULT_LLM_MODELS)
        selected_prompt = st.selectbox('Choose prompt:', PROMPTS_CONFIG.keys())
        selected_testcases = st.multiselect(
            "Choose testcases:",
            TESTCASES_LIST,
            TESTCASES_LIST
        )
        submitted = st.form_submit_button("Let's test")

        if submitted:
            with st.spinner("Fetching data..."):
                short_response, long_response = async_get_test(
                    prompt_number=selected_prompt,
                    llm_model=selected_llm,
                    testcases=selected_testcases
                )
            st.subheader("Short Result: ")
            st.write(short_response)
            st.subheader("------------------------------------------------------------")
            st.subheader("Long Result: ")
            st.write(long_response)

    st.header("Testcases Preview")
    for index, specification, expected_result in TESTCASES_LIST:
        st.text_area(f"Testcase-{index}: ", value=specification, height=350)
        st.text_area(f"Expected Result-{index}: ", value=expected_result, height=30)


if __name__ == "__main__":
    main()
