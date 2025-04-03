from abc import ABC, abstractmethod
from typing import Any

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
    def parse_version(cls, value: Any) -> Version:
        if isinstance(value, Version):
            version = value
        else:
            version = Version(value)
        expected_major = cls._get_version().major
        if expected_major != version.major:
            raise ValueError(f"schemaVersion {value} does not match expected major version '{expected_major}'")
        return version
