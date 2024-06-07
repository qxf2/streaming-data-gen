"""
Module for generating a continuous stream of data points with random anomalies
based on specified parameters.
"""

import random
import asyncio
import logging
from app.models.anomaly_models import RandomAnomalyModel


logger = logging.getLogger(__name__)


async def generate_random_anomalies(random_anomaly: RandomAnomalyModel):
    """
    Generates data points with random anomalies.

    Args:
        random_anomaly (RandomAnomalyModel): The model containing the parameters
                                    for generating the random anomalies.

    Yields:
        str: A string representation of a data point.
    """
    try:
        while True:
            if random.random() < random_anomaly.anomaly_probability:
                anomaly = random.uniform(
                    -random_anomaly.anomaly_range, random_anomaly.anomaly_range
                )
                anomaly_value = random_anomaly.base_value + anomaly
            else:
                anomaly_value = random_anomaly.base_value
            yield f"{anomaly_value:.3f}\n"
            await asyncio.sleep(random_anomaly.data_interval)
    except asyncio.CancelledError:
        logger.info("Data generation was cancelled.")
    except Exception as error:
        logger.exception("Error occurred while generating data: %s", error)
        raise
