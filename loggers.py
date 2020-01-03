import logging

logs_out = ''


def get_logger(name):

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        # Prevent logging from propagating to the root logger
        logger.propagate = 0
        ch = logging.StreamHandler()

        if name.startswith('test'):
            logs_out = 'testlogs.log'
        else:
            logs_out = 'logs.log'

        fh = logging.FileHandler(filename=logs_out)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)
        logger.addHandler(ch)
        logger.addHandler(fh)
    return logger
