from typing import Dict, Type

from pydantic import BaseModel

from .export import export_schema as _export_schema
from .models.v0.edp import ExtendedDatasetProfile as ExtendedDatasetProfileV0
from .models.version import SchemaVersion as SchemaVersion

CURRENT_SCHEMA = ExtendedDatasetProfileV0

schema_versions: Dict[SchemaVersion, Type[BaseModel]] = {SchemaVersion.V0: ExtendedDatasetProfileV0}


def export_schema():
    return _export_schema(CURRENT_SCHEMA)
