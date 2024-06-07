"""
Module for generateing data points with regular spikes occurring at
specified interval within a duration of 1 hour.
"""

import random
import asyncio
import logging
import itertools
from app.models.anomaly_models import SpikeAnomalyModel

logger = logging.getLogger(__name__)


async def generate_periodic_spike_data(spike_anomaly: SpikeAnomalyModel):
    """
    Generates data points with spikes at regular intervals.

    Args:
        spike_anomaly (SpikeAnomalyModel): The model containing the parameters
            used for generating the data.

    Yields:
        str: A string representation of a data point.
    """
    try:
        total_time_seconds = 30
        for each_val in itertools.count():
            current_time = (each_val + 1) % total_time_seconds
            if current_time % spike_anomaly.spike_interval == 0 and current_time != 0:
                spike_value = random.uniform(spike_anomaly.min_spike_range, spike_anomaly.max_spike_range)
                yield f"{spike_value:.3f}\n"
            else:
                yield f"{spike_anomaly.base_value:.3f}\n"
            await asyncio.sleep(spike_anomaly.data_interval)
    except asyncio.CancelledError:
        logger.info("Data generation was cancelled.")
    except Exception as error:
        logger.exception("Error occurred while generating data: %s", error)
        raise
