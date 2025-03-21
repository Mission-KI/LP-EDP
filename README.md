# Extended Dataset Profile

The Extended Data Profile provides a common module with all versions of
the EDP pydantic model. This module is shared between daseen &amp; EDPS.

# Using this library

## Library Installation

You can the install this package in your project with the UV package manager,
but any python package manager should work. We advice to always specify a
tag, so your builds stay reproducible:

```bash
# With UV package manager
uv add <URL> --tag <TAG>

# or with poetry
poetry install <URL>

# or with conda
conda install <URL>

# or with PIP
pip install <URL>
```

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

# Developer Info

## Clone and install repository

The project's dependencies are managed via the uv package manager. Even though, the pyproject.toml is
compliant to other package managers as well, but you might need to add a reference to the pytorch
package sources when installing. We advice using the uv package manager for increased speed and
better support of the pyproject.toml.

[Here you can find information on how to install uv.](https://docs.astral.sh/uv/getting-started/installation)
I strongly advice NOT to install ANYTHING with `pip install uv` in a hosts main python installation.

After you installed uv, you can install this repository as follows. The command will create a ".venv" directory
inside your repository:

```bash
git clone <URL>
cd extended_dataset_profile_service
uv sync --all-extras
```

For linting we use pre-commit. You can enable checking all commits by running this command inside your repository
directory:
```bash
uv run pre-commit install
```

We utilize pytest for the unit tests. You can run the test either through your IDE's test section, or by calling:
```sh
uv run pytest .
```

## Adding a new (major) version

1. _major version only_: define the new model in a new version directory like
`src/extended_dataset_profile/models/v2`.
2. _major version only_: extend the `schema_versions` dictionary with by the major
version and the new model.
3. add a new git tag to automatically specify the `schemaVersion` used for the
current EDP pydantic model.

## Writing your own schema

You can create your own schema by forking this repository.
We advice you delete all schemas except the most recent one and start from there.

Keep in mind, that the tests check for the schema being compatible to elastic search indexing.
This means, all keys in the resulting JSON need to be static. Keys must not be set dynamically
by your creating tool. If this does not matter for you, feel free to delete the test.
