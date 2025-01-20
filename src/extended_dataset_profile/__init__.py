from enum import Enum
from typing import Dict, Type

from pydantic import BaseModel

from .models.v1.edp import ExtendedDatasetProfile as ExtendedDatasetProfileV0


class SchemaVersion(str, Enum):
    V0 = "v0"


schema_versions: Dict[SchemaVersion, Type[BaseModel]] = {SchemaVersion.V0: ExtendedDatasetProfileV0}
