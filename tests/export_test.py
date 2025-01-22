import sys
from pathlib import Path

from pytest import MonkeyPatch

from extended_dataset_profile.models.v1.edp import export_edp_schema


def test_export_edp_schema(tmp_path: Path, monkeypatch: MonkeyPatch):
    schema_file = tmp_path / "schema.json"
    monkeypatch.setattr(sys, "argv", [__name__, "--output", str(schema_file)])
    export_edp_schema()
    assert schema_file.exists()
