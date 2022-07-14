"""
This is a boilerplate pipeline 'data_proccesing'
generated using Kedro 0.18.1
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import convert


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=convert,
                inputs="json_dataset",
                outputs="raw_binary",
                name="convert",
            )
        ]
    )
