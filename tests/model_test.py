import typing
from datetime import datetime, timedelta
from enum import Enum
from pathlib import PurePosixPath
from types import NoneType
from typing import Literal, Union, get_args, get_origin
from uuid import UUID

import pytest
from pydantic import AnyUrl, BaseModel

from extended_dataset_profile import CURRENT_SCHEMA, schema_versions
from extended_dataset_profile.models.v0.edp import Numeric
from extended_dataset_profile.models.v0.languages import Language
from extended_dataset_profile.types.version import Version

EXPLICITLY_ALLOWED_TYPES = [
    NoneType,
    str,
    int,
    float,
    complex,
    bool,
    datetime,
    timedelta,
    PurePosixPath,
    AnyUrl,
    UUID,
    Version,
]


# This tests, whether the EDP is always index able with a finite amount of indices.
def test_finite_edp_index():
    for schema in schema_versions.values():
        _assert_has_static_indices_only(schema)


def _assert_has_static_indices_only(current_type: type):
    """Check if the given type is valid for the EDPS model (it must not allow custom indices for fields)."""

    if current_type in EXPLICITLY_ALLOWED_TYPES:
        return
    elif get_origin(current_type) == Literal:
        return
    elif isinstance(current_type, type) and issubclass(current_type, Enum):
        return
    elif isinstance(current_type, type) and issubclass(current_type, BaseModel):
        for field_name, field in current_type.model_fields.items():
            field_type = field.annotation
            if field_type is None:
                raise TypeError(
                    f'The field "{field_name}" inside the pydantic model "{current_type}" is missing a type annotation!'
                )
            _assert_has_static_indices_only(field_type)
    elif current_type is Language:
        return
    elif get_origin(current_type) in [tuple, typing.Tuple]:
        args = get_args(current_type)
        if (len(args) == 2) and ((None in args) or (NoneType in args)):
            # Special case for Optional
            for arg in args:
                _assert_has_static_indices_only(arg)
        else:
            raise TypeError("Tuples can not get indexed by elastic, since it thinks they are heterogenous arrays.s")
    elif get_origin(current_type) in [list, set, tuple]:
        for generic_type in get_args(current_type):
            _assert_has_static_indices_only(generic_type)
    elif get_origin(current_type) is dict:
        raise TypeError(
            f'Found forbidden type dictionary: "{current_type}". These would lead to an index explosion in Elastic.'
        )
    elif get_origin(current_type) is Union:
        # Special case for optional, which is allowed. get_origin(Optional) will always result in Union.
        args = get_args(current_type)
        if len(args) == 2:
            if None in args:
                return
            if NoneType in args:
                return

        # Special case for numeric, which is the only Union we currently allow.
        if current_type is Numeric:
            return

        raise TypeError(
            f'Found forbidden type union: "{current_type}". These would lead to the same JSON keys containing different types of objects.'
        )
    else:
        raise NotImplementedError(f'The check for "{current_type}" is not yet implemented.')


def test_schema_version_major_mismatch_error():
    with pytest.raises(ValueError, match="schemaVersion 1.0.0 does not match expected major version '0'"):
        CURRENT_SCHEMA.model_validate(
            {
                "schemaVersion": "1.0.0",
                "name": "test",
                "generatedBy": "test",
                "freely_available": True,
                "volume": 1,
                "assetSha256Hash": "test",
            }
        )
