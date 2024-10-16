import pandas

from metrics import get_selected_metrics
from datasets import CustomEvaluationDataset


def test_dataset_with_metrics(
    testcases_dataset: pandas.DataFrame, metrics_dict: dict, columns_dict: dict
):
    dataset = CustomEvaluationDataset()
    dataset.add_test_cases_from_dataframe(testcases_dataset, **columns_dict)
    metrics_list = get_selected_metrics(metrics_dict)
    results = dataset.evaluate(metrics_list)
    return results
