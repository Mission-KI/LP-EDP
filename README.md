# Extended Dataset Profile

The Extended Data Profile provides a common module with all versions of
the EDP pydantic model. This module is shared between daseen &amp; EDPS.

## Usage

`extended_dataset_profile` provides a `schema_versions` dictionary which maps
from a specific version to a pydantic model.

```python
from extended_dataset_profile import schema_versions, SchemaVersion
edp_model = schema_versions[SchemaVersion.V0]

edp_data={...}

edp_model(**edp_data) # validation
```

## Adding a new Version

1. define the new model in a new version directory (e.g. `v5`) in
`src/extended_dataset_profile/models`.
2. extend the SchemaVersion enum by your new version
3. add the import and extend the `schema_versions` in the
`src/extended_dataset_profile/__init__.py`.
