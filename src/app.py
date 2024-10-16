import deepeval
import streamlit as st
import pandas as pd

from langsmith import Client as LangsmithClient

from metrics import METRICS_DICT
from utils import run_async_in_sync
from inputs import TESTCASES_LIST
from csv_utils import get_prompts_config
from main import test_prompt, get_df_results_of_testing
from metrics_evaluation import test_dataset_with_metrics
from streamlit_tools import display_metric_results, get_feedback_form, call_llm_form
from config import (
    OPENROUTER_DEFAULT_LLM_MODELS,
    PATH_TO_PROMPT_CSV_FILE,
    DEFAULT_MANUAL_TESTING_CONFIG,
)
from llm_calls import (
    call_llm_with_langsmith_monitoring,
    call_llm_with_deepeval_monitoring,
)


def prompt_testing_section(prompts_config):
    """
    Displays the section of the application where users can test prompts
    with different LLM models and predefined test cases. Users can select
    a model, a specific prompt, and test cases from a list to evaluate
    the model's performance. Once the form is submitted, it fetches the
    LLM responses, compares them to expected results, and displays the
    short and long format results in the Streamlit interface.

    Args:
        prompts_config (dict): Configuration for prompts including template, instruction, and options.
    """

    st.header("Test your prompt")

    with st.form("test_prompt_form"):
        selected_llm = st.selectbox("Choose LLM model: ", OPENROUTER_DEFAULT_LLM_MODELS)
        selected_prompt_number = st.selectbox("Choose prompt:", prompts_config)
        selected_testcases = st.multiselect(
            "Choose testcases:", TESTCASES_LIST, TESTCASES_LIST
        )
        submitted = st.form_submit_button("Let's test")

        if submitted:
            prompt_template = st.session_state.get(
                f"prompt_template-{selected_prompt_number}"
            )
            prompt_instruction = st.session_state.get(
                f"instruction-{selected_prompt_number}"
            )
            prompt_options = st.session_state.get(f"options-{selected_prompt_number}")

            with st.spinner("Fetching data..."):
                short_response, long_response, passed_testcases = run_async_in_sync(
                    function=test_prompt,
                    prompt_number=selected_prompt_number,
                    prompt_template=prompt_template,
                    prompt_instruction=prompt_instruction,
                    prompt_options=prompt_options,
                    llm_model=selected_llm,
                    testcases=selected_testcases,
                )
            failed_testcases = len(selected_testcases) - passed_testcases
            st.subheader(
                f"Short Result: :green[{passed_testcases} passed], :red[{failed_testcases} failed]"
            )
            st.write(short_response)
            st.markdown(
                "<hr style='border:3px dashed black;margin:20px 0;'>",
                unsafe_allow_html=True,
            )
            st.subheader("Long Result: ")
            st.write(long_response)

    st.header("Prompts")

    for prompt_number, prompt_config in prompts_config.items():
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


def deepeval_testing_section(prompts_config):
    """
    Displays the section where users can test LLM responses with custom
    evaluation metrics using DeepEval. Users can upload a CSV file for
    batch evaluation or manually select test cases for evaluation.
    The system will apply user-selected metrics to evaluate LLM
    performance and display detailed results, showing where the model
    met or failed the expected outcomes.

     Args:
         prompts_config (dict): Configuration for prompts including template, instruction, and options.
    """

    testcases_df = None

    st.header("Test your LLM responses with custom metrics")

    if "columns_config" not in st.session_state:
        st.session_state.columns_config = {}
    if "metrics_config" not in st.session_state:
        st.session_state.metrics_config = {}

    def update_metrics():
        for metric_name in st.session_state.metrics:
            if metric_name not in st.session_state.metrics_config:
                st.session_state.metrics_config[metric_name] = 0.5

    selected_metrics = st.multiselect(
        "Choose metrics:", METRICS_DICT.keys(), key="metrics", on_change=update_metrics
    )

    if selected_metrics:
        for metric in selected_metrics:
            st.subheader(f"Settings for {metric}")

            threshold = st.slider(
                f"Set threshold for {metric}:",
                min_value=0.0,
                max_value=1.0,
                value=st.session_state.metrics_config[metric],
                key=f"slider_{metric}",
            )

            st.session_state.metrics_config[metric] = threshold

    uploaded_file = st.file_uploader(
        f"Upload CSV file for evaluation", type="csv", key=f"eval_file"
    )
    if uploaded_file:
        # Read the CSV file and display a preview
        testcases_df = pd.read_csv(uploaded_file)
        st.write(f"CSV File Preview for evaluation:")
        st.write(testcases_df.head())

        st.write("**CSV Evaluation settings:**")
        # Set column configuration for further evaluation
        input_columns = [None] + list(testcases_df.columns)
        input_col_name = st.selectbox(
            f"Select Input Column",
            input_columns,
            key=f"input_col",
        )
        actual_output_col_name = st.selectbox(
            f"Select Actual Output Column",
            input_columns,
            key=f"actual_output_col",
        )
        expected_output_col_name = st.selectbox(
            f"Select Expected Output Column",
            input_columns,
            key=f"expected_output_col",
        )
        context_col_name = st.selectbox(
            f"Select Context Column",
            input_columns,
            key="context_column",
        )
        additional_metadata_col_name = st.selectbox(
            f"Select Additional Metadata Column",
            input_columns,
            key="additional_metadata_col_name",
        )
        st.session_state.columns_config = {
            "input_col_name": input_col_name,
            "actual_output_col_name": actual_output_col_name,
            "expected_output_col_name": expected_output_col_name,
            "context_col_name": context_col_name,
            "additional_metadata_col_name": additional_metadata_col_name,
        }

    st.write("**Manual Evaluation settings:**")
    selected_llm = st.selectbox("Choose LLM model: ", OPENROUTER_DEFAULT_LLM_MODELS)
    selected_prompt_number = st.selectbox("Choose prompt:", prompts_config)
    selected_testcases = st.multiselect("Choose testcases:", TESTCASES_LIST)
    col1, col2 = st.columns(2)

    with col1:
        with st.form("csv_test_form"):
            csv_testing = st.form_submit_button(
                "📄ㅤ**Evaluate CSV**",
                use_container_width=True,
            )
    with col2:
        with st.form("manual_test_form"):
            manual_testing = st.form_submit_button(
                "🛠️ㅤ**Manual Evaluation**",
                use_container_width=True,
            )

    if csv_testing:
        if not selected_metrics:
            st.error(f"No metrics uploaded!")
            return None
        if not uploaded_file or testcases_df.empty:
            st.error(f"No CSV file uploaded!")
            return None

        with st.spinner(f"Evaluating CSV file"):
            results_of_evaluating_df = test_dataset_with_metrics(
                testcases_dataset=testcases_df,
                metrics_dict=st.session_state.metrics_config,
                columns_dict=st.session_state.columns_config,
            )

        st.subheader(f"Results of evaluating LLM:")

        for index, evaluation_result in enumerate(results_of_evaluating_df):
            testcase = testcases_df[
                testcases_df[st.session_state.columns_config["input_col_name"]]
                == evaluation_result.input
            ]
            metadata_col = st.session_state.columns_config[
                "additional_metadata_col_name"
            ]
            expected_result_col = st.session_state.columns_config[
                "expected_output_col_name"
            ]

            if metadata_col:
                st.write(
                    f"-\n\t\t\tTESTCASE-{testcase[metadata_col].values[0]} | "
                    f"Expected: {testcase[expected_result_col].values[0]} "
                )
            display_metric_results(evaluation_result.metrics_data)
            st.success("✅ㅤCSV Evaluation completed")

    if manual_testing:
        if not selected_metrics:
            st.error(f"No metrics uploaded!")
            return None
        if not selected_testcases:
            st.error(f"No testcases chosen!")
            return None

        st.session_state.columns_config = DEFAULT_MANUAL_TESTING_CONFIG

        prompt_template = st.session_state.get(
            f"prompt_template-{selected_prompt_number}"
        )
        prompt_instruction = st.session_state.get(
            f"instruction-{selected_prompt_number}"
        )
        prompt_options = st.session_state.get(f"options-{selected_prompt_number}")

        with st.spinner("Fetching data..."):
            results_of_testing_df = run_async_in_sync(
                function=get_df_results_of_testing,
                prompt_template=prompt_template,
                prompt_instruction=prompt_instruction,
                prompt_options=prompt_options,
                llm_model=selected_llm,
                testcases=selected_testcases,
            )
            st.write(f"Results of testing LLM:")
            st.write(results_of_testing_df)

            results_of_evaluating_df = test_dataset_with_metrics(
                results_of_testing_df,
                metrics_dict=st.session_state.metrics_config,
                columns_dict=st.session_state.columns_config,
            )

            st.subheader(f"Results of evaluating LLM:")

            for index, evaluation_result in enumerate(results_of_evaluating_df):
                testcase = results_of_testing_df[
                    results_of_testing_df["Specification"] == evaluation_result.input
                ]
                st.write(
                    f"-\n\t\t\tTESTCASE-{testcase['Testcase'].values[0]} | "
                    f"Expected: {testcase['Expected Result'].values[0]}"
                )
                display_metric_results(evaluation_result.metrics_data)
        st.success("✅ㅤManual Evaluation completed.")


def testcases_section():
    """Displays a Streamlit section for viewing test cases."""
    st.header("Testcases")

    for index, expected_result, specification in TESTCASES_LIST:
        st.text_area(
            f"Testcase-{index}: ", value=specification, height=350, key=f"spec_{index}"
        )
        st.text_area(
            f"Expected Result-{index}: ",
            value=expected_result,
            height=30,
            key=f"expected_{index}",
        )
        st.markdown("---")


def monitoring_section():
    """
    Displays a section for monitoring LLM responses using two different
    monitoring frameworks: Langsmith and DeepEval. Users can submit
    prompts to the LLM, view the LLM's response, and track
    completion time and costs in app or in the framework.
    After receiving responses, users can provide feedback on the correctness of the outputs and submit this
    feedback directly to the monitoring systems (Langsmith or DeepEval).
    """

    col1, col2 = st.columns(2)

    with col1:
        name_of_first_framework = "Langsmith 🦜"
        response_form_langsmith = call_llm_form(
            name_of_first_framework, call_llm_with_langsmith_monitoring
        )
        if response_form_langsmith:
            _, llm_response, completion_time, total_cost, run_id = (
                response_form_langsmith
            )
            st.write(f"**Response LLM:** \n{llm_response}")
            st.write(f"**Completion Time:** {completion_time:.2f}s")
            st.write(f"**Total Cost:** {total_cost:.2f}s")

            get_feedback_form(name_of_first_framework, llm_response)

            def send_feedback_to_langsmith():
                langsmith_client = LangsmithClient()
                langsmith_client.create_feedback(
                    run_id,
                    key="Correctness",
                    score=st.session_state[f"rating_{name_of_first_framework}"] / 5,
                    comment=st.session_state[f"feedback_{name_of_first_framework}"],
                    correction={
                        "Expected result": st.session_state[
                            f"expected_response_{name_of_first_framework}"
                        ]
                    },
                )

            st.button("Send feedback!", on_click=send_feedback_to_langsmith)

    with col2:
        name_of_second_framework = "DeepEval 🔮"

        response_form_deepeval = call_llm_form(
            name_of_second_framework, call_llm_with_deepeval_monitoring
        )
        if response_form_deepeval:
            _, llm_response, completion_time, total_cost, run_id = (
                response_form_deepeval
            )
            st.write(f"**Response LLM:** \n{llm_response}")
            st.write(f"**Completion Time:** {completion_time:.2f}s")
            st.write(f"**Total Cost:** {total_cost:.2f}s")

            get_feedback_form(name_of_second_framework, llm_response)

            def send_feedback_to_deepeval():
                deepeval.send_feedback(
                    response_id=run_id,
                    rating=st.session_state[f"rating_{name_of_second_framework}"],
                    explanation=st.session_state[f"feedback_{name_of_second_framework}"],
                    expected_response=st.session_state[
                        f"expected_response_{name_of_second_framework}"
                    ],
                )
                st.success("Successfully sent feedback!")

            st.button("Send feedback!", on_click=send_feedback_to_deepeval)


def main():
    """
    The main function initializes and configures the Streamlit application.
    It sets up tabs for various sections, including Prompt Testing, DeepEval
    Testing, Testcases, and Monitoring. This function loads the prompt
    configurations and controls the flow between different sections of
    the app, rendering the relevant interfaces for user interaction.
    """

    st.set_page_config(page_title="Prompt Test", layout="wide")

    st.markdown(
        """
        <style>
        .center-title {
            text-align: center;
        }
        </style>
        <h1 class="center-title">Prompt Test App</h1>
        """,
        unsafe_allow_html=True,
    )

    prompts_config = get_prompts_config(PATH_TO_PROMPT_CSV_FILE)

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "🔍 **Prompt Testing**",
            "🧪 **DeepEval Testing**",
            "📊 **Testcases**",
            "💬 **DeepEval and Langsmith Monitoring**",
        ]
    )

    with tab1:
        prompt_testing_section(prompts_config)
    with tab2:
        deepeval_testing_section(prompts_config)
    with tab3:
        testcases_section()
    with tab4:
        monitoring_section()


if __name__ == "__main__":
    main()
