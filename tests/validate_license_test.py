import pytest

from extended_dataset_profile.models.v0.edp import License, validate_license


def test_validate_license():
    validate_license(License(url="http://mylicense.com"))
    validate_license(License(name="MIT"))
    validate_license(License(name="MIT", url="http://mylicense.com"))


def test_validate_license_required():
    with pytest.raises(ValueError, match="License model needs at least 'name' or 'url'"):
        validate_license(License())
