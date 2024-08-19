import asyncio
import streamlit as st

from config import OPENROUTER_DEFAULT_LLM_MODELS, PATH_TO_PROMPT_CSV_FILE
from inputs import TESTCASES_LIST
from main import test_prompt
from utils import get_prompts_config


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

    PROMPTS_CONFIG = get_prompts_config(PATH_TO_PROMPT_CSV_FILE)

    with st.form("my_form"):
        selected_llm = st.selectbox("Choose LLM model: ", OPENROUTER_DEFAULT_LLM_MODELS)
        selected_prompt_number = st.selectbox("Choose prompt:", PROMPTS_CONFIG)
        selected_testcases = st.multiselect(
            "Choose testcases:", TESTCASES_LIST, TESTCASES_LIST
        )
        submitted = st.form_submit_button("Let's test")

        if submitted:
            prompt_template = st.session_state.get(f"prompt_template-{selected_prompt_number}")
            prompt_instruction = st.session_state.get(f"instruction-{selected_prompt_number}")
            prompt_options = st.session_state.get(f"options-{selected_prompt_number}")

            with st.spinner("Fetching data..."):
                short_response, long_response = async_get_test(
                    prompt_number=selected_prompt_number,
                    prompt_template=prompt_template,
                    prompt_instruction=prompt_instruction,
                    prompt_options=prompt_options,
                    llm_model=selected_llm,
                    testcases=selected_testcases,
                )
            st.subheader("Short Result: ")
            st.write(short_response)
            st.markdown(
                "<hr style='border:3px dashed black;margin:20px 0;'>",
                unsafe_allow_html=True
            )
            st.subheader("Long Result: ")
            st.write(long_response)

    st.header("Prompts")

    for prompt_number, prompt_config in PROMPTS_CONFIG.items():
        st.text_area(
            f"**{prompt_number.upper()}**",
            value=prompt_config["prompt_template"],
            key=f"prompt_template-{prompt_number}",
            height=350,
        )
        st.text_area(
            f"Instruction: ",
            value=prompt_config["instruction"],
            key=f"instruction-{prompt_number}",
            height=300,
        )
        st.text_area(
            f"Options: ",
            value=prompt_config["options"],
            key=f"options-{prompt_number}",
            height=200,
        )

    st.header("Testcases")
    for index, specification, expected_result in TESTCASES_LIST:
        st.text_area(f"Testcase-{index}: ", value=specification, height=350)
        st.text_area(f"Expected Result-{index}: ", value=expected_result, height=30)


if __name__ == "__main__":
    main()
