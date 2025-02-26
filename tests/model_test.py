from datetime import datetime, timedelta, timezone
from enum import Enum
from logging import getLogger
from pathlib import PurePosixPath
from types import NoneType
from typing import Literal, Union, get_args, get_origin
from uuid import UUID

from pydantic import AnyUrl, BaseModel

from extended_dataset_profile import SchemaVersion, schema_versions
from extended_dataset_profile.models.v0.edp import DataSpace, License, Publisher, UserProvidedEdpData
from extended_dataset_profile.models.v0.languages import Language

logger = getLogger(__name__)


# This tests, whether the EDP is always index able with a finite amount of indices.
def test_finite_edp_index():
    models_already_processed: set[type[BaseModel]] = set()
    models_to_process: list[type[BaseModel]] = [schema_versions[SchemaVersion.V0]]

    while len(models_to_process) != 0:
        model = models_to_process.pop(0)
        if model not in models_already_processed:
            models_to_process.extend(_validate_model(model))
            models_already_processed.add(model)


def _validate_model(model_type: type[BaseModel]):
    logger.info("Checking model %s", model_type.__name__)
    for field_name, field in model_type.__pydantic_fields__.items():
        field_type = field.annotation
        if field_type:
            try:
                yield from _validate_model_type(field_type)
            except TypeError as e:
                raise TypeError(f"{model_type.__name__}.{field_name}: Type {e} is not supported in the schema!")


# Check if the given type is valid for the EDPS model (it must not allow custom indices for fields) and return
# additional types that need checking.
def _validate_model_type(current_type: type):
    if current_type in [NoneType, str, int, float, complex, bool, datetime, timedelta, PurePosixPath, AnyUrl, UUID]:
        pass
    elif get_origin(current_type) == Literal:
        pass
    elif isinstance(current_type, type) and issubclass(current_type, Enum):
        pass
    elif isinstance(current_type, type) and issubclass(current_type, BaseModel):
        yield current_type
    elif current_type is Language:
        pass
    elif get_origin(current_type) in [Union, list, set]:
        for generic_type in get_args(current_type):
            yield from _validate_model_type(generic_type)
    else:
        raise TypeError(str(current_type))


def test_recursively_escape_strings():
    user_provided_data = UserProvidedEdpData(
        assetId="my-dataset-id",
        name="Hello <script>alert('XSS');</script>",
        url="https://beebucket.ai/en/",
        dataCategory="TestDataCategory",
        dataSpace=DataSpace(name="Hello <script>alert('XSS');</script>", url="https://beebucket.ai/en/"),
        publisher=Publisher(name="beebucket"),
        license=License(url="https://opensource.org/license/mit"),
        description="Our very first test edp",
        publishDate=datetime(year=1995, month=10, day=10, hour=10, tzinfo=timezone.utc),
        version="2.3.1",
        tags=["test", "Hello <script>alert('XSS');</script>"],
        freely_available=True,
    )
    expected_escaped = "Hello &lt;script&gt;alert(&#x27;XSS&#x27;);&lt;/script&gt;"

    assert user_provided_data.name == expected_escaped
    assert user_provided_data.dataSpace.name == expected_escaped
    assert user_provided_data.tags[1] == expected_escaped
