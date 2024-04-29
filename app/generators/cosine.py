"""
Module for generating a cosine wave data stream based on the given CosineModel parameters.
"""

import asyncio
import logging
import numpy as np
from app.models.waveform_models import CosineModel

logger = logging.getLogger(__name__)

async def generate_cosine_data(cosine_model: CosineModel):
    """
    Generates a cosine wave data stream based on the given Cosine model parameters.

    Args:
        cosine_model (CosineModel): The model containing the parameters
                                    for generating the cosine wave.
    Yields:
        str: A string representation of a data point in the cosine wave.
    """

    time_index = 0
    while True:
        try:
            data_point = cosine_model.amplitude * np.cos(
                2 * np.pi * cosine_model.frequency * (time_index / cosine_model.sample_rate)
            )
            yield f"{data_point:.3f}\n"
            await asyncio.sleep(cosine_model.interval)
            time_index += 1
        except ValueError as value_error:
            logger.error("Value error occurred while generating cosine wave: %s", value_error)
            continue
        except asyncio.CancelledError:
            logger.info("Cosine wave generation was cancelled.")
            break
        except Exception as error:
            logger.exception("An unexpected error occurred while generating cosine wave: %s", error)
            raise
