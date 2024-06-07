"""
Module for generating a specified number of anomalies within a fixed duration (1 hour).
"""

import random
import asyncio
import logging
import itertools
from app.models.anomaly_models import CountBasedAnomalyModel

logger = logging.getLogger(__name__)


async def generate_count_based_anomalies_data(
    count_based_anomaly: CountBasedAnomalyModel,
):
    """
    Generates data points with specified number of anomalies within a duration of 1 hour.

    Args:
        count_based_anomaly (CountBasedAnomalyModel): The model containing the parameters
            used for generating the data.

    Yields:
        str: A string representation of a data point.
    """
    try:
        total_time_seconds = 30
        anomaly_start_times = sorted(
            random.sample(range(total_time_seconds), count_based_anomaly.num_anomalies)
        )

        for x in itertools.count():
            current_time = x % total_time_seconds
            if current_time in anomaly_start_times:
                anomaly_value = random.uniform(
                    count_based_anomaly.min_anomaly_range,
                    count_based_anomaly.max_anomaly_range,
                )
                yield f"{anomaly_value:.3f}\n"
            else:
                yield f"{count_based_anomaly.base_value:.3f}\n"
            await asyncio.sleep(count_based_anomaly.data_interval)
    except asyncio.CancelledError:
        logger.info("Data generation was cancelled.")
    except Exception as error:
        logger.exception("Error occurred while generating data: %s", error)
        raise
