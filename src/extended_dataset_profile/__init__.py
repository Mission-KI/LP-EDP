from typing import Dict, Type

from pydantic import BaseModel

from .models.v1.edp import ExtendedDatasetProfile as ExtendedDatasetProfileV0
from .models.version import SchemaVersion as SchemaVersion

schema_versions: Dict[SchemaVersion, Type[BaseModel]] = {SchemaVersion.V0: ExtendedDatasetProfileV0}
