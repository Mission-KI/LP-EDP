from abc import ABC, abstractmethod
from typing import Any

from packaging.version import InvalidVersion
from pydantic import BaseModel, Field, field_validator

from extended_dataset_profile.types.version import Version


class ExtendedDatasetProfileBase(ABC, BaseModel):
    @staticmethod
    @abstractmethod
    def _get_version() -> Version: ...

    schemaVersion: Version = Field(
        default_factory=_get_version,
        description="Version of the JSON Schema used to generate this EDP",
    )

    @field_validator("schemaVersion", mode="before")
    @classmethod
    def parse_version(cls, value: Any) -> str:
        if isinstance(value, str):
            major = cls._get_version().major
            try:
                if major != Version(value).major:
                    raise ValueError(f"schemaVersion {value} does not match expected major version '{major}'")
                return value
            except InvalidVersion:
                raise ValueError(f"Invalid schema version '{value}'")
        raise ValueError(f"Invalid schema version '{value}'")
