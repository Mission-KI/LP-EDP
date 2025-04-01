import pytest
from packaging.version import Version as BuiltInVersion
from pydantic import TypeAdapter

from extended_dataset_profile.types import Version


@pytest.fixture(scope="session")
def adapter():
    return TypeAdapter(Version)


def test_version_parses_from_str(adapter):
    adapter.validate_strings("1.2.3")


def test_version_validates_builtin_version(adapter):
    adapter.validate_python(BuiltInVersion("1.2.3"))


def test_version_validates_our_version(adapter):
    adapter.validate_python(Version("1.2.3"))


def test_version_serializes_python(adapter):
    python_dump = adapter.dump_python(Version("1.2.3"))
    assert isinstance(python_dump, Version)
    assert isinstance(python_dump, BuiltInVersion)


def test_version_serializes_json(adapter):
    json_bytes = adapter.dump_json(Version("1.2.3"))
    json = json_bytes.decode()
    assert isinstance(json, str)
    assert json == '"1.2.3"'
