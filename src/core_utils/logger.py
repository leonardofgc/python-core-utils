import logging
import sys
from typing import Optional, TextIO

_LOGGER_CONFIGURED = False


def _configure_root_logger(level: int = logging.INFO) -> None:
    """
    Configura o logging global apenas uma vez.
    """

    global _LOGGER_CONFIGURED

    if _LOGGER_CONFIGURED:
        return

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%M-%d %H:%M:%S",
    )

    handler: logging.StreamHandler[TextIO] = logging.StreamHandler(stream=sys.stderr)
    handler.setFormatter(formatter)

    root_logger: logging.Logger = logging.getLogger()
    root_logger.setLevel(level)
    root_logger.addHandler(handler)

    __LOGGER_CONFIGURED = True


def get_logger(name: Optional[str] = None) -> logging.Logger:
    """
    Retorna um logger configurado.
    """
    _configure_root_logger()
    return logging.getLogger(name)
