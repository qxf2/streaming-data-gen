"""
Module for generating random positive square wave anomalies with
varying durations at irregular intervals.
"""

import random
import asyncio
import logging
from app.models.anomaly_models import RandomSquareModel

logger = logging.getLogger(__name__)


async def generate_random_square(square_model: RandomSquareModel):
    """
    Generates data points with random square wave anomalies.


    Yields:
        str: A string representation of a data point.
    """

    logger.info(
        "Generating data with random square wave anomalies with parameters: %s",
        square_model,
    )
    anomaly_countdown = random.randint(
        square_model.minimum_interval, square_model.maximum_interval
    )
    anomaly_end = 0

    try:
        while True:
            if anomaly_countdown <= 0:
                anomaly_countdown = random.randint(
                    square_model.minimum_interval, square_model.maximum_interval
                )
                anomaly_duration = random.randint(
                    square_model.min_anomaly_duration, square_model.max_anomaly_duration
                )
                anomaly_end = anomaly_duration

            if anomaly_end > 0:
                anomaly_value = square_model.base_value + square_model.anomaly_magnitude
                yield f"{anomaly_value:.3f}\n"
                anomaly_end -= 1
            else:
                yield f"{square_model.base_value:.3f}\n"
                anomaly_countdown -= 1

            await asyncio.sleep(square_model.data_interval)
    except asyncio.CancelledError:
        logger.info("Data generation was cancelled.")
    except Exception as error:
        logger.exception("Error occurred while generating data: %s", error)
        raise
