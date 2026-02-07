from core_utils.logger import get_logger


def test_get_logger_returns_logger():
    logger = get_logger(__name__)
    assert logger.name == __name__


def test_logger_emits_message(caplog):
    """
    caplog é fixture poderosa do pytest para capturar logs.
    """
    logger = get_logger(__name__)

    with caplog.at_level("INFO"):
        logger.info("mensagem de teste")

    assert "mensagem de teste" in caplog.text
