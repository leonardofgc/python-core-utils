import pytest

from core_utils.validators import validate_not_empty
from core_utils.exceptions import ValidationError

def test_validate_not_empty_success():
    assert validate_not_empty("Leonardo", "nome") == "Leonardo"


def test_validate_not_empty_raise_error():
    with pytest.raises(ValidationError):
        validate_not_empty(" ", "nome")