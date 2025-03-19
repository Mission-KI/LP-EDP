# Extended Dataset Profile

The Extended Data Profile provides a common module with all versions of
the EDP pydantic model. This module is shared between daseen &amp; EDPS.

## Usage

`extended_dataset_profile` provides a `schema_versions` dictionary which maps
from a specific version to a pydantic model.

```python
from extended_dataset_profile import schema_versions, CURRENT_SCHEMA
from packaging.version import Version

# getting a specific version
edp_model = schema_versions[Version(0, 1, 0)]

# getting the current version
edp_model = CURRENT_SCHEMA

edp_data={...}

edp_model(**edp_data) # validation
```

## Adding a new (major) version

1. _major version only_: define the new model in a new version directory like
`src/extended_dataset_profile/models/v2`.
2. _major version only_: extend the `schema_versions` dictionary with by the major
version and the new model.
3. add a new git tag to automatically specify the `schemaVersion` used for the
current EDP pydantic model.
