import sys
from pathlib import Path

from pytest import MonkeyPatch

from extended_dataset_profile.models.v1.edp import export_edp_schema


def test_export_edp_schema(tmp_path: Path, monkeypatch: MonkeyPatch):
    monkeypatch.setattr(sys, "argv", [__name__, "--output", str(tmp_path / "schema.json")])
    export_edp_schema()
