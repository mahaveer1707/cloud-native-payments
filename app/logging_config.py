import logging
from pythonjsonlogger.json import JsonFormatter
import os

def setup_logging():
    logger = logging.getLogger()
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
    logger.setLevel(getattr(logging, LOG_LEVEL, logging.INFO))

    handler = logging.StreamHandler()
    formatter = JsonFormatter(
        "%(asctime)s %(levelname)s %(name)s %(message)s"
    )
    handler.setFormatter(formatter)

    logger.handlers = []
    logger.addHandler(handler)