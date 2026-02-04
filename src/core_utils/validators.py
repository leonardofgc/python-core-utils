from core_utils.exceptions import ValidationError

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
        raise ValidationError(f"O campo '{field_name}' não pode ser vazio")
    
    return value