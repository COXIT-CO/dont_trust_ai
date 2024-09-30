import pandas as pd

from typing import Optional
from deepeval.dataset import EvaluationDataset
from deepeval.test_case import LLMTestCase


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
        additional_metadata_col_name: Optional[str] = None,
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

        additional_metadatas = [
            {"Testcase": str(metadata)} if metadata else None
            for metadata in get_column_data(
                df, additional_metadata_col_name, default=""
            )
        ]

        for (
            input,
            actual_output,
            expected_output,
            context,
            retrieval_context,
            additional_metadata,
        ) in zip(
            inputs,
            actual_outputs,
            expected_outputs,
            contexts,
            retrieval_contexts,
            additional_metadatas,
        ):
            self.add_test_case(
                LLMTestCase(
                    input=input,
                    actual_output=actual_output,
                    expected_output=expected_output,
                    context=context,
                    retrieval_context=retrieval_context,
                    additional_metadata=additional_metadata,
                )
            )
