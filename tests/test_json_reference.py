import pytest

from extended_dataset_profile.models.v1.json_reference import JsonReference


def test_json_reference_does_not_match_empty():
    with pytest.raises(ValueError):
        JsonReference(reference="")


def test_json_reference_does_not_match_exclamation_mark():
    with pytest.raises(ValueError):
        JsonReference(reference="#/!joa")


def test_json_reference_does_not_match_empty_path_segment():
    with pytest.raises(ValueError):
        JsonReference(reference="#/hello/world//")


def test_json_reference_matches_path():
    JsonReference(reference="#/hello/world")


def test_json_reference_matches_path_with_indices():
    JsonReference(reference="#/hello/world/1")


def test_json_reference_matches_path_with_underscore():
    JsonReference(reference="#/hello_world")


def test_json_reference_matches_path_with_minus():
    JsonReference(reference="#/hello-world")
