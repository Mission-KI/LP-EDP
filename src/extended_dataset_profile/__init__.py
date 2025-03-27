from typing import Dict, Type

from .export import export_schema as _export_schema
from .models.base import ExtendedDatasetProfileBase

# import all models from the v0 version as this is the current version
from .models.v0 import *  # noqa: F403
from .models.v0 import ExtendedDatasetProfile
from .version import CURRENT_VERSION
from .version import __version__ as __version__

schema_versions: Dict[int, Type[ExtendedDatasetProfileBase]] = {CURRENT_VERSION.major: ExtendedDatasetProfile}

CURRENT_SCHEMA = schema_versions[CURRENT_VERSION.major]


def export_schema():
    return _export_schema(CURRENT_SCHEMA)
