import pytest

from core_utils.exceptions import ValidationError
from core_utils.validators import (
    validate_email,
    validate_not_empty,
    validate_positive_number,
)


def test_validate_not_empty_success():
    assert validate_not_empty("Leonardo", "nome") == "Leonardo"


def test_validate_not_empty_raise_error():
    with pytest.raises(ValidationError):
        validate_not_empty(" ", "nome")


@pytest.mark.parametrize("value", [1, 10, 0.5, 999])
def test_validate_positive_number_success(value):
    assert validate_positive_number(value, "preco") == value


@pytest.mark.parametrize("value", [0, -1, -50])
def test_validate_positive_number_error(value):
    with pytest.raises(ValidationError):
        validate_positive_number(value, "preco")


@pytest.mark.parametrize(
    "email", ["user@email.com", "teste.silva@gmail.com", "dev123@empresa.com"]
)
def test_validate_email_success(email):
    assert validate_email(email) == email


@pytest.mark.parametrize(
    "email", ["useremail.com", "user@", "@gmail.com", "email-invalido"]
)
def test_validate_email_error(email):
    with pytest.raises(ValidationError):
        validate_email(email)
