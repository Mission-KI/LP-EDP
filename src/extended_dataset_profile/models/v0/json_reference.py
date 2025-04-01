import re
from typing import Any

from pydantic import AliasChoices, BaseModel, Field, field_validator

_JSON_KEY_CHARACTERS = r"a-zA-Z0-9_-"
_JSON_REFERENCE_REGEX = re.compile(f"#(\\/[{_JSON_KEY_CHARACTERS}]+)+")


class JsonReference(BaseModel):
    """
    A reference to another field within the same JSON file.
    """

    reference: str = Field(
        serialization_alias="$ref",
        validation_alias=AliasChoices("$ref", "reference"),
        description="The JSON keys that lead to the referred value.",
    )

    @field_validator("reference", mode="after")
    @classmethod
    def _validate_json_reference(cls, value: Any):
        if not isinstance(value, str):
            raise ValueError("Json reference must be of type str")
        if _JSON_REFERENCE_REGEX.fullmatch(value) is None:
            raise ValueError(f'The string "{value}" is not a JSON reference!')
        return value
