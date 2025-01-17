import functools
import logging
import colorlog

"""Логгер, и декоратор для логирования ошибок и успешного прохождения тестов"""



logger = logging.getLogger(__name__)

formatter = colorlog.ColoredFormatter(
    '%(log_color)s%(asctime)s  - %(levelname)s:%(message)s',
    log_colors={
        'DEBUG': 'white',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white',
    },
    secondary_log_colors={},
    style='%'
)

console = logging.StreamHandler()
console.setFormatter(formatter)
logger.addHandler(console)
logger.setLevel(logging.DEBUG)


def error_handler(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            logger.info(f"Function {func.__name__} executed successfully.")
        except Exception as e:
            logger.error(f"Error: {e}", exc_info=True)

    return wrapper
