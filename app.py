from books_reccomender.exception.exception_handler import AppException
import sys

from books_reccomender.logger.log import logging

try:
    a = 3 / 0
except Exception as e:
    logging.info(e)
    raise AppException(e, sys) from e
