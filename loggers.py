import logging


logs_out = ''

def get_logger(name):
    """Custom logger.

    Function for custom logging.
    Args:
        name: name of current module

    Returns:
        logger: logging object

    """

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        # Prevent logging from propagating to the root logger
        logger.propagate = 0

        console_handler = logging.StreamHandler()

        if name.startswith('test'):
            logs_out = 'testlogs.log'
        else:
            logs_out = 'logs.log'

        file_handler = logging.FileHandler(filename=logs_out)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger
