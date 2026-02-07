class CoreUtilsError(Exception):
    """
    Erro base da biblioteca core_utils.
    Tudo que der errado aqui deve herdar dele.
    """

    pass


class ValidationError(CoreUtilsError):
    """
    Erro lançado quando um dado não é válido.
    """

    pass
