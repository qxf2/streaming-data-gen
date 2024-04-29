"""
Module for generating a sine wave data stream based on the given SineModel parameters.
"""

import asyncio
import logging
import numpy as np
from app.models.waveform_models import SineModel


logger = logging.getLogger(__name__)


async def generate_sine_data(sine_model: SineModel):
    """
    Generates a sine wave data stream based on the given Sine model parameters.

    Args:
        sine_model (SineModel): The model containing the parameters for generating the sine wave.

    Yields:
        str: A string representation of a data point in the sine wave.
    """

    time_index = 0
    while True:
        try:
            data_point = sine_model.amplitude * np.sin(
                2 * np.pi * sine_model.frequency * (time_index / sine_model.sample_rate)
                + sine_model.phase
            )
            yield f"{data_point:.3f}\n"
            await asyncio.sleep(sine_model.interval)
            time_index += 1
        except ValueError as value_error:
            logger.error(
                "Value error occurred while generating sine wave: %s", value_error
            )
            continue
        except asyncio.CancelledError:
            logger.info("Sine wave generation was cancelled.")
            break
        except Exception as error:
            logger.exception("An unexpected error occurred while generating sine wave: %s", error)
            raise
