import streamlit as st

from typing import Callable

from utils import run_async_in_sync
from config import DEFAULT_PROMPT_FOR_MONITORING, DEFAULT_LLM_MODEL_FOR_MONITORING


def get_result_word(expected: str, obtained: str):
    """
    Compare if expected sentence is in obtained
    and return the result word in Streamlit format
    """
    if expected in obtained:
        return ":green[success]"
    return ":red[failed]"


def display_metric_results(metrics):
    for metric in metrics:
        status_of_testing = (
            ":green[✅ Success]" if metric.success else ":red[❌ Failed]"
        )

        st.write(
            f"**📝 Metric Name:** {metric.name} | "
            f"**📊 Threshold:** {metric.threshold:.2f} | "
            f"**⭐ Score:** {metric.score:.2f} | "
            f"**🤖 Evaluation Model:** {metric.evaluation_model}"
        )

        if metric.error:
            st.write(f"**❗ Error:** {metric.error}")

        st.write(f"**💡 Reason:** {metric.reason}")
        st.write(f"**💰 Evaluation Cost:** {metric.evaluation_cost:.6f} USD")
        st.write(f"**Result:** {status_of_testing}")
        st.write("---")


def call_llm_form(framework_name: str, function_for_call: Callable):

    st.title(f"Chatbot with {framework_name}")

    cabinet_specification = st.text_area(
        "**🗄️ Enter specification of cabinet**",
        height=200,
        key=f"specification_{framework_name}",
    )

    if st.button(
        "Send to LLM",
        use_container_width=True,
        type="primary",
        key=f"llm_response_with_{framework_name}",
    ):
        if cabinet_specification:
            prompt_template = st.session_state.get(
                f"prompt_template-{DEFAULT_PROMPT_FOR_MONITORING}"
            )
            prompt_instruction = st.session_state.get(
                f"instruction-{DEFAULT_PROMPT_FOR_MONITORING}"
            )
            prompt_options = st.session_state.get(
                f"options-{DEFAULT_PROMPT_FOR_MONITORING}"
            )

            with st.spinner("Fetching data..."):
                return run_async_in_sync(
                    function=function_for_call,
                    prompt_template=prompt_template,
                    instruction=prompt_instruction,
                    options=prompt_options,
                    input_text=cabinet_specification,
                    llm_model=DEFAULT_LLM_MODEL_FOR_MONITORING,
                )
        else:
            st.warning("Please, enter specification of cabinet!")


def get_feedback_form(framework_name: str, llm_response: str):
    if f"rating_{framework_name}" not in st.session_state:
        st.session_state[f"rating_{framework_name}"] = 3
    if f"feedback_{framework_name}" not in st.session_state:
        st.session_state[f"feedback_{framework_name}"] = ""
    if f"expected_result_{framework_name}" not in st.session_state:
        st.session_state[f"expected_result_{framework_name}"] = llm_response

    with st.form(key=f"feedback_form_{framework_name}"):
        st.write("Rate the response:")
        st.session_state[f"rating_{framework_name}"] = st.slider(
            "Mark (1-5)",
            value=st.session_state[f"rating_{framework_name}"],
            min_value=1,
            max_value=5,
            key=f"slider_mark_{framework_name}",
        )

        st.session_state[f"feedback_{framework_name}"] = st.text_area(
            "Feedback (optional):",
            value=st.session_state[f"feedback_{framework_name}"],
            height=100,
            key=f"expected_feedback_{framework_name}",
        )

        st.session_state[f"expected_result_{framework_name}"] = st.text_area(
            "Expected result (optional):",
            value=st.session_state[f"expected_result_{framework_name}"],
            height=100,
            key=f"expected_response_{framework_name}",
        )
        st.form_submit_button("")
