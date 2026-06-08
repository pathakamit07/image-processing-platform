import logging
import json


logging.basicConfig(
    level=logging.INFO,
    format="%(message)s"
)

logger = logging.getLogger(
    "image-processing"
)


def log_json(data):

    logger.info(
        json.dumps(data)
    )