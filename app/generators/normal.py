"""
Module for generating a normal distribution data stream based on the given NormalModel parameters.
"""

import asyncio
import logging
from scipy.stats import norm
from app.models.distribution_models import NormalModel

logger = logging.getLogger(__name__)


async def generate_normal_data(normal_model: NormalModel):
    """
    Generates a normal distribution data stream based on the given Normal model parameters.

    Args:
        normal_model (NormalModel): The model containing the parameters for
                                    generating the normal distribution.
    Yields:
        str: A string representation of a data point in the normal distribution.
    """
    while True:
        try:
            data_point = norm.rvs(loc=normal_model.mean, scale=normal_model.std_dev)
            yield f"{data_point:.3f}\n"
            await asyncio.sleep(normal_model.interval)
        except ValueError as value_error:
            logger.error(
                "Value error occurred while generating normal distribution: %s", value_error)
            continue
        except asyncio.CancelledError:
            logger.info("Normal distribution data generation was cancelled.")
            break
        except Exception as error:
            logger.exception(
                "An unexpected error occurred while generating normal distribution data: %s", error)
            raise
