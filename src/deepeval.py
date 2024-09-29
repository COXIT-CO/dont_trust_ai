import pandas

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
)
from metrics import CorrectnessMetric, CustomEvaluationDataset


def get_selected_metrics(selected_metrics: dict):
    available_metrics = {
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
    return [
        available_metrics[metric](threshold=threshold)
        for metric, threshold in selected_metrics.items()
    ]


def test_dataset_with_metrics(
    testcases_dataset: pandas.DataFrame, metrics_dict: dict, columns_dict: dict
):
    dataset = CustomEvaluationDataset()
    dataset.add_test_cases_from_dataframe(testcases_dataset, **columns_dict)
    metrics_list = get_selected_metrics(metrics_dict)
    results = dataset.evaluate(metrics_list)
    return results
