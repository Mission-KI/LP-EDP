from pydantic_markdown import document_model
from pytest import fixture

from extended_dataset_profile import ExtendedDatasetProfile


@fixture
def output_markdown(tmp_path):
    with open(tmp_path / "model_doc.md", "wt", encoding="utf-8") as file:
        yield file


def test_config_doc_is_complete(output_markdown):
    document_model(output_markdown, ExtendedDatasetProfile)
