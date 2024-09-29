from typing import Optional

import pandas as pd
from deepeval.dataset import EvaluationDataset
from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCaseParams, LLMTestCase


class CustomEvaluationDataset(EvaluationDataset):
    def add_test_cases_from_dataframe(
        self,
        df: pd.DataFrame,
        input_col_name: str,
        actual_output_col_name: str,
        expected_output_col_name: Optional[str] = None,
        context_col_name: Optional[str] = None,
        context_col_delimiter: str = ";",
        retrieval_context_col_name: Optional[str] = None,
        retrieval_context_col_delimiter: str = ";",
    ):
        """
        Load test cases from a Pandas Dataframe.
        """

        def get_column_data(df: pd.DataFrame, col_name: str, default=None):
            return (
                df[col_name].values if col_name in df.columns else [default] * len(df)
            )

        inputs = get_column_data(df, input_col_name)
        actual_outputs = get_column_data(df, actual_output_col_name)
        expected_outputs = get_column_data(df, expected_output_col_name, default=None)
        contexts = [
            context[0].split(context_col_delimiter) if context else []
            for context in get_column_data(df, context_col_name, default="")
        ]
        retrieval_contexts = [
            (
                retrieval_context.split(retrieval_context_col_delimiter)
                if retrieval_context
                else []
            )
            for retrieval_context in get_column_data(
                df, retrieval_context_col_name, default=""
            )
        ]

        for (
            input,
            actual_output,
            expected_output,
            context,
            retrieval_context,
        ) in zip(
            inputs,
            actual_outputs,
            expected_outputs,
            contexts,
            retrieval_contexts,
        ):
            self.add_test_case(
                LLMTestCase(
                    input=input,
                    actual_output=actual_output,
                    expected_output=expected_output,
                    context=context,
                    retrieval_context=retrieval_context,
                )
            )


class CorrectnessMetric(GEval):
    def __init__(self, threshold: float = 0.5):
        super().__init__(
            name="Correctness",
            criteria="Ensure that the result series match the expected result series",
            evaluation_steps=[
                "1. Verify that the core material is correctly chosen according to the expected result.",
                "2. Verify that the material for fronts is selected correctly, according to the expected result.",
                "3. Verify that the material for ends is selected correctly, according to the expected result.",
                "4. Verify that the correct edging is selected, according to the expected result.",
                "5. Verify that the cabinet edgebanding matches the expected result.",
            ],
            evaluation_params=[
                LLMTestCaseParams.INPUT,
                LLMTestCaseParams.ACTUAL_OUTPUT,
                LLMTestCaseParams.EXPECTED_OUTPUT,
            ],
            threshold=threshold,
        )


# List of available metrics
METRICS_LIST = [
    "Correctness",
    "Answer Relevancy",
    "Faithfulness",
    "Hallucination",
    "Summarization",
    "Toxicity",
    "Bias",
    "Contextual Recall",
    "Contextual Relevancy",
    "Contextual Precision",
]
