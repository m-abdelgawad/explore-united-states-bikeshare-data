from datetime import datetime
import logging

# Import logger
logger = logging.getLogger()


def get_current():
    logger.info("Execute timestamp module...")
    return str(datetime.now().strftime("%Y-%m-%d__%H-%M-%S"))
