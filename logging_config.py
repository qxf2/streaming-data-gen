"""
Logging configuration for the FastAPI Data Streaming Application.
"""

import logging
import os

def setup_logging():
    try:
        # Define the base directory and log file path
        base_dir = os.path.dirname(os.path.abspath(__file__))
        log_file_path = os.path.join(base_dir, "app.log")

        # Configure the root logger
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        if logger.hasHandlers():
            logger.handlers.clear()

        # Create console handler with a normal formatter
        c_handler = logging.StreamHandler()
        c_format = logging.Formatter(
            "%(asctime)s loglevel=%(levelname)-6s logger=%(name)s %(funcName)s() L%(lineno)-4d %(message)s"
        )
        c_handler.setFormatter(c_format)
        c_handler.setLevel(logging.DEBUG)

        # Create file handler with a detailed formatter
        f_handler = logging.FileHandler(log_file_path)
        f_format = logging.Formatter(
            "%(asctime)s loglevel=%(levelname)-6s logger=%(name)s %(funcName)s() L%(lineno)-4d %(message)s   call_trace=%(pathname)s L%(lineno)-4d"
        )
        f_handler.setFormatter(f_format)
        f_handler.setLevel(logging.DEBUG)

        # Add handlers to the root logger
        logger.addHandler(c_handler)
        logger.addHandler(f_handler)

        return logger
    except Exception as e:
        print(f"Failed to configure logging: {e}")
        raise

# Call the setup function and get the configured logger
logger = setup_logging()
