"""
Module for generating clustered anomalies occuring at random intervals.
"""

import random
import asyncio
import logging
from app.models.anomaly_models import ClusteredAnomalyModel

logger = logging.getLogger(__name__)


async def generate_clustered_anomalies(clustered_model: ClusteredAnomalyModel):
    """
    Generates data points with clustered anomalies.

    Args:
        clustered_model (ClusteredAnomalyModel): The model containing the parameters
            used for generating the data.

    Yields:
        str: A string representation of a data point.
    """
    anomaly_countdown = random.randint(clustered_model.minimum_interval, clustered_model.maximum_interval)
    anomaly_length = 0

    try:
        while True:
            if anomaly_countdown <= 0:
                anomaly_countdown = random.randint(
                    clustered_model.minimum_interval, clustered_model.maximum_interval
                )
                anomaly_length = random.randint(
                    clustered_model.min_anomaly_length,
                    clustered_model.max_anomaly_length,
                )

            if anomaly_length > 0:
                anomaly_value = clustered_model.constant_value + random.uniform(
                    -clustered_model.anomaly_magnitude,
                    clustered_model.anomaly_magnitude,
                )
                yield f"{anomaly_value:.3f}\n"
                anomaly_length -= 1
            else:
                yield f"{clustered_model.constant_value:.3f}\n"
                anomaly_countdown -= 1

            await asyncio.sleep(clustered_model.data_interval)
    except asyncio.CancelledError:
        logger.info("Data generation was cancelled.")
    except Exception as error:
        logger.exception("Error occurred while generating data: %s", error)
        raise
