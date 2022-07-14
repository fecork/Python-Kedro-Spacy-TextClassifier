"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline, pipeline

from text_classifier_spacy.pipelines import data_proccesing as dp


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """

    data_proccesing = dp.create_pipeline()

    return {"__default__": data_proccesing, "dp": data_proccesing}
