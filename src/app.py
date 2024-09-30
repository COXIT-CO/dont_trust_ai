import asyncio
import streamlit as st
import pandas as pd

from config import OPENROUTER_DEFAULT_LLM_MODELS, PATH_TO_PROMPT_CSV_FILE
from inputs import TESTCASES_LIST
from main import test_prompt, get_df_results_of_testing
from metrics_evaluation import test_dataset_with_metrics
from metrics import METRICS_DICT
from utils import get_prompts_config


def run_async_in_sync(function, *args, **kwargs):
    """
    Function to run the async code within the synchronous Streamlit context
    """
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop.run_until_complete(function(*args, **kwargs))


def prompt_testing_section(prompts_config):
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


def deepeval_testing_section(prompts_config):
    st.header("Test your LLM responses with custom metrics")

    if "columns_info" not in st.session_state:
        st.session_state.columns_info = {
            "input_col_name": "Specification",
            "actual_output_col_name": "LLM Response",
            "expected_output_col_name": "Expected Result",
            "context_col_name": "Prompt",
            "additional_metadata_col_name": "Testcase",
        }
    if "metrics_info" not in st.session_state:
        st.session_state.metrics_info = {}

    def update_metrics():
        for metric_name in st.session_state.metrics:
            if metric_name not in st.session_state.metrics_info:
                st.session_state.metrics_info[metric_name] = 0.5

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
                value=st.session_state.metrics_info[metric],
                key=f"slider_{metric}",
            )

            st.session_state.metrics_info[metric] = threshold

    uploaded_file = st.file_uploader(
        f"Upload CSV file for evaluation", type="csv", key=f"eval_file"
    )
    if uploaded_file:
        # Read the CSV file and display a preview
        testcases_df = pd.read_csv(uploaded_file)
        st.write(f"CSV File Preview for evaluation:")
        st.write(testcases_df.head())

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
        st.session_state.columns_info = {
            "input_col_name": input_col_name,
            "actual_output_col_name": actual_output_col_name,
            "expected_output_col_name": expected_output_col_name,
            "context_col_name": context_col_name,
            "additional_metadata_col_name": additional_metadata_col_name,

        }
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

    if csv_testing:

        if not selected_metrics:
            st.error(f"No metrics uploaded!")
            return None
        if not uploaded_file:
            st.error(f"No CSV file uploaded!")
            return None

        with st.spinner(f"Evaluating CSV file"):
            results_of_evaluating_df = test_dataset_with_metrics(
                testcases_dataset=testcases_df,
                metrics_dict=st.session_state.metrics_info,
                columns_dict=st.session_state.columns_info,
            )

            testcases_metadata_list = []
            metadata_col_name = st.session_state.columns_info["additional_metadata_col_name"]

            if metadata_col_name:
                testcases_metadata_list = testcases_df[metadata_col_name].tolist()
            st.subheader(f"Results of evaluating LLM:")

            for index, evaluation_result in enumerate(results_of_evaluating_df):
                testcase_metadata = testcases_metadata_list[index] if testcases_metadata_list else index
                st.write(f"-\n\t\t\tTESTCASE-{testcase_metadata}: ")
                display_metric_results(evaluation_result.metrics_data)

        st.success("✅ㅤCSV Evaluation completed")

    with col2:
        with st.form("manual_test_form"):
            manual_testing = st.form_submit_button(
                "🛠️ㅤ**Manual Evaluation**",
                use_container_width=True,
            )

    if manual_testing:

        if not selected_metrics:
            st.error(f"No metrics uploaded!")
            return None

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
                metrics_dict=st.session_state.metrics_info,
                columns_dict=st.session_state.columns_info,
            )

            testcases_list = results_of_testing_df["Testcase"].tolist()
            st.subheader(f"Results of evaluating LLM:")

            for index, evaluation_result in enumerate(results_of_evaluating_df):
                st.write(f"-\n\t\t\tTESTCASE-{testcases_list[index]}: ")
                display_metric_results(evaluation_result.metrics_data)

        st.success("✅ㅤManual Evaluation completed.")


def testcases_section():
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


def main():
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
    # Load prompts configuration
    prompts_config = get_prompts_config(PATH_TO_PROMPT_CSV_FILE)

    tab1, tab2, tab3 = st.tabs(
        ["🔍 **Prompt Testing**", "🧪 **DeepEval Testing**", "📊 **Testcases**"]
    )

    with tab1:
        prompt_testing_section(prompts_config)
    with tab2:
        deepeval_testing_section(prompts_config)
    with tab3:
        testcases_section()


if __name__ == "__main__":
    main()
