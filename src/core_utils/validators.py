from typing import Union
import re
from core_utils.exceptions import ValidationError
from core_utils.logger import get_logger

logger = get_logger(__name__)

EMAIL_REGEX = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")

def validate_not_empty(value: str, field_name: str) -> str:
    """
    Valida se um campo string não está vazio.

    Args:
        value: valor recebido
        field_name: nome do campo para mensagens claras

    Returns:
        O valor validado

    Raises:
        ValidationError: se estiver vazio
    """

    if not value or not value.strip():
        logger.warning("Campo vazio detectado: %s", field_name)
        raise ValidationError(f"O campo '{field_name}' não pode ser vazio.")
    
    return value


def validate_positive_number(value: Union[int, float], field_name: str) -> Union[int, float]:
    """
    Garante que um número é positivo (> 0).
    """

    if value <= 0:
        logger.warning("Número não positivo para %s: %s", field_name, value)
        raise ValidationError(f"O campo '{field_name}' deve ser um número positivo.")
    
    return value

def validate_email(email: str) -> str:
    """
    Valida formato básico de email.
    """

    if not EMAIL_REGEX.match(email):
        logger.warning("Email inválido recebido: %s", email)
        raise ValidationError("Email Inválido")
    
    return email