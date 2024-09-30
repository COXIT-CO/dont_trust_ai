from deepeval.metrics import (
    AnswerRelevancyMetric,
    FaithfulnessMetric,
    HallucinationMetric,
    SummarizationMetric,
    ToxicityMetric,
    BiasMetric,
    ContextualRelevancyMetric,
    ContextualRecallMetric,
    ContextualPrecisionMetric,
    GEval,
)

from deepeval.test_case import LLMTestCaseParams

# Constants
DEFAULT_THRESHOLD = 0.5


class CorrectnessMetric(GEval):
    """
    Metric for evaluating correctness by ensuring that the selected
    result matches the expected result based on a series of material
    selection steps.
    """

    def __init__(self, threshold: float = DEFAULT_THRESHOLD):
        super().__init__(
            model="gpt-4o-mini",
            name="Correctness",
            criteria="Ensure that the result series match the expected result series.",
            evaluation_steps=[
                "Verify that the core material is correctly chosen according to the expected result.",
                "Verify that the material for fronts is selected correctly, according to the expected result.",
                "Verify that the material for ends is selected correctly, according to the expected result.",
                "Verify that the correct edging is selected, according to the expected result.",
                "Verify that the cabinet edgebanding matches the expected result.",
            ],
            evaluation_params=[
                LLMTestCaseParams.ACTUAL_OUTPUT,
                LLMTestCaseParams.EXPECTED_OUTPUT,
            ],
            threshold=threshold,
        )


# List of available metrics
METRICS_DICT = {
    "Correctness": CorrectnessMetric,
    "Answer Relevancy": AnswerRelevancyMetric,
    "Faithfulness": FaithfulnessMetric,
    "Hallucination": HallucinationMetric,
    "Summarization": SummarizationMetric,
    "Toxicity": ToxicityMetric,
    "Bias": BiasMetric,
    "Contextual Recall": ContextualRecallMetric,
    "Contextual Relevancy": ContextualRelevancyMetric,
    "Contextual Precision": ContextualPrecisionMetric,
}


def get_selected_metrics(selected_metrics: dict):
    """
    Retrieve the selected metrics with their associated thresholds.

    Args:
        selected_metrics (dict): Dictionary of selected metrics with threshold values.

    Returns:
        list: A list of instantiated metric objects.
    """

    return [
        METRICS_DICT[metric](threshold=threshold)
        for metric, threshold in selected_metrics.items()
    ]


