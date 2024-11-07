import logging
import functools

def get_logger():
    logger = logging.getLogger('flask-cms')
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger

def log_method(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger = get_logger()
        logger.info(f'Entering {func.__name__}')
        try:
            result = func(*args, **kwargs)
            logger.info(f'Exiting {func.__name__}')
            return result
        except Exception as e:
            logger.error(f'Error in {func.__name__}: {str(e)}')
            raise
    return wrapper 