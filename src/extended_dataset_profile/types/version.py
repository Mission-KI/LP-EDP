from typing import Any, Union

from packaging.version import Version as _BuiltinVersion
from pydantic import GetCoreSchemaHandler
from pydantic_core import core_schema as cs


class Version(_BuiltinVersion):
    """
    Semantic version inheriting the packaging version class with added pydantic parsing.
    """

    @classmethod
    def __get_pydantic_core_schema__(cls, source: type[Any], handler: GetCoreSchemaHandler) -> cs.CoreSchema:
        return cs.no_info_plain_validator_function(
            cls._validate,
            json_schema_input_schema=cs.str_schema(),
            serialization=cs.plain_serializer_function_ser_schema(
                cls._serialize_json, when_used="json", info_arg=False, return_schema=cs.str_schema()
            ),
        )

    @classmethod
    def _validate(cls, object: Union[_BuiltinVersion, "Version", Any]) -> "Version":
        if isinstance(object, Version):
            return object
        if isinstance(object, _BuiltinVersion):
            return Version(str(object))
        return Version(object)

    @classmethod
    def _serialize_json(cls, instance: "Version"):
        return str(instance)
