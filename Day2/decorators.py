import operator
import random
import os
import re
from collections import defaultdict

from datetime import datetime
import time
import functools

import logging

# Create a logger
logger = logging.getLogger('my_logger')
logger.setLevel(logging.WARNING)

# Create a file handler
file_handler = logging.FileHandler('my_log_file.log')
file_handler.setLevel(logging.DEBUG)

# Create a formatter and set it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(file_handler)




def log_errors(funkcja):
    @functools.wraps(funkcja)
    def wrapper(*args, **kwargs):
        try:
            logger.info(f'Arguments for call {funkcja.__name__} ({args}, {kwargs})')
            funkcja(*args, **kwargs)
        except ValueError as e:
            logger.error(f'Byl blad {e}')
        except IOError as e:
            logger.warning(f'wiadomosc inna {e}')

    return wrapper


@log_errors
def do_opakowania(x : int):
    if x == 10:
        raise ValueError("Dla 10 nie dzialam")
    if x == 5:
        raise IOError("blad polaczenia")
    return x


if __name__ == '__main__':
    do_opakowania(5)
    do_opakowania(10)
    do_opakowania(6)


    # Stwórz dekorator limit_calls który ogranicza liczbę wywołań danej funkcji.
    # Jeśli funkcja zostanie wywołana więcej razy niż dozwolone, dekorator powinien zwrócić komunikat o błędzie.
    