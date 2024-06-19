

print("Hello world from __init__.py")

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

from .functions import times3

__author__ = "Wojciech"

__doc__ = "Tu wpiszemy dokumentacje modułu"

__all__ = ["times3"]