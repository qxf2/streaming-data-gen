"""
Module for generating a sawtooth wave data stream based on the given SawtoothModel parameters.
"""

import asyncio
import logging
import numpy as np
from app.models.waveform_models import SawtoothModel

logger = logging.getLogger(__name__)


async def generate_sawtooth_data(sawtooth_model: SawtoothModel):
    """
    Generates a sawtooth wave data stream based on the given Sawtooth model parameters.

    Args:
        sawtooth_model (SawtoothModel): The model containing the parameters for
                                        generating the Sawtooth distribution.

    Yields:
        str: A string representation of a data point in the Sawtooth distribution.
    """

    time_index = 0
    while True:
        try:
            cycles = (
                2 * np.pi *
                sawtooth_model.frequency *
                (time_index / sawtooth_model.sample_rate)
            )
            data_point = sawtooth_model.amplitude * (cycles - np.floor(cycles))
            yield f"{data_point:.3f}\n"
            await asyncio.sleep(sawtooth_model.interval)
            time_index += 1
        except ValueError as value_error:
            logger.error(
                "Value error occurred while generating sawtooth wave: %s", value_error
            )
            continue
        except asyncio.CancelledError:
            logger.info("Sawtooth wave generation was cancelled.")
            break
        except Exception as error:
            logger.exception("An unexpected error occurred while generating sawtooth wave: %s", error)
            raise
