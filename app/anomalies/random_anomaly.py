"""
Module for generating random anomalies.
"""

import random
import asyncio
import logging
from .anomalies_interface import AnomalyGenerator

logger = logging.getLogger(__name__)

class RandomAnomalyGenerator(AnomalyGenerator):
    """
    Class for generating random anomalies.
    """

    def __init__(self, c, anomaly_probability, anomaly_range, data_interval):
        """
        Initializes the RandomAnomalyGenerator.

        Args:
            c (float): Base value around which anomalies will occur.
            anomaly_probability (float): Probability of an anomaly occurring.
            anomaly_range (float): Range within which anomalies can vary.
            data_interval (float): Time interval between data points.
        """
        self.base_value = c
        self.anomaly_probability = anomaly_probability
        self.anomaly_range = anomaly_range
        self.data_interval = data_interval

    async def generate_data(self):
        """
        Generates data points with random anomalies.

        Yields:
            str: A string representation of a data point.
        """
        try:
            while True:
                if random.random() < self.anomaly_probability:
                    anomaly = random.uniform(-self.anomaly_range, self.anomaly_range)
                    anomaly_value = self.base_value + anomaly
                else:
                    anomaly_value = self.base_value
                yield f"{anomaly_value:.3f}\n"
                await asyncio.sleep(self.data_interval)
        except asyncio.CancelledError:
            logger.info("Data generation was cancelled.")
        except Exception as error:
            logger.exception("Error occurred while generating data: %s", error)
            raise
        