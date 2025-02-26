from pydantic import BaseModel
from pytest import raises

from extended_dataset_profile.models.v0.languages import Language, is_iso639_3


class Model(BaseModel):
    language: Language


def test_is_iso639_3():
    assert is_iso639_3("deu")
    assert not is_iso639_3("blabla")
    assert not is_iso639_3("en")


def test_annotated_language_type():
    Model(language="deu")


def test_language_type_only_set3():
    with raises(ValueError):
        Model(language="en")


def test_language_type_doesnt_accept_free_text():
    with raises(ValueError):
        Model(language="blalba")


def test_language_type_case_insensitive():
    model = Model(language="Deu")
    assert model.language == "deu"
