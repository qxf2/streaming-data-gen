"""
Module for generating a square wave data stream with a specified amplitude change duration.
"""

import itertools
import random
import asyncio
import logging
from .anomalies_interface import AnomalyGenerator

logger = logging.getLogger(__name__)

class SquareWaveGenerator(AnomalyGenerator):
    """
    Anomaly generator for generating a square wave data stream
    with a specified amplitude change duration.

    Attributes:
        base_value (float): The base value for regular data points.
        duration (int): The duration of the square wave signal in seconds.
        interval (float): The rate at which data points are generated.
        amplitude_change (float): The amplitude change value during the specified duration.
    """
    def __init__(self, c, duration, interval, amplitude_change):
        self.base_value = c
        self.duration = duration
        self.interval = interval
        self.amplitude_change = amplitude_change

    async def generate_data(self):
        """
        Generates a square wave data stream with a specified amplitude change duration.

        Yields:
            str: A string representation of a data point in the square wave.
        """
        try:
            total_time_seconds = 3600
            start_time = random.randint(0, total_time_seconds - self.duration)
            end_time = start_time + self.duration

            for current_time in itertools.count():
                current_time = current_time % total_time_seconds
                if start_time <= current_time < end_time:
                    data_value = self.base_value + self.amplitude_change
                else:
                    data_value = self.base_value
                yield f"{data_value:.3f}\n"
                await asyncio.sleep(self.interval)
        except asyncio.CancelledError:
            logger.info("Data generation coroutine was cancelled.")
        except Exception as error:
            logger.exception("Error occurred while generating data: %s", error)
            raise
        