"""
Module for generating a square wave data stream based on the given SquareModel parameters.
"""

import asyncio
import logging
import numpy as np
from scipy.signal import square
from app.models.waveform_models import SquareModel

logger = logging.getLogger(__name__)


async def generate_square_data(square_model: SquareModel):
    """
    Generates square wave data based on the given Square model parameters.

    Args:
        square_model (SquareModel): The model containing the parameters for
                                    generating the square wave.

    Yields:
        str: A string representation of a data point in the square wave.
    """
    time_index = 0
    while True:
        try:
            data_point = square(
                2 * np.pi *
                square_model.frequency *
                (time_index / square_model.sample_rate)
            )
            yield f"{data_point:.3f}\n"
            await asyncio.sleep(square_model.interval)
            time_index += 1
        except ValueError as value_error:
            logger.error(
                "Value error occurred while generating square wave: %s", value_error
            )
            continue
        except asyncio.CancelledError:
            logger.info("Square wave generation was cancelled.")
            break
        except Exception as error:
            logger.exception("An unexpected error occurred while generating square wave: %s", error)
            raise
