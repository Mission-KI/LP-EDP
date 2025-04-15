import pytest

from extended_dataset_profile.models.v1.edp import License


def test_validate_license():
    License(url="http://mylicense.com")
    License(name="MIT")
    License(name="MIT", url="http://mylicense.com")


def test_validate_license_required():
    with pytest.raises(ValueError, match="License model needs at least 'name' or 'url'"):
        License()
