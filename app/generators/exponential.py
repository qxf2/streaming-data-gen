"""
Module for generating an exponential distribution data stream based on the
given ExponentialModel parameters.
"""

import asyncio
import logging
from scipy.stats import expon
from app.models.distribution_models import ExponentialModel

logger = logging.getLogger(__name__)


async def generate_exponential_data(exponential_model: ExponentialModel):
    """
    Generates exponential data stream based on the given Exponential model parameters.

    Parameters:
        exponential_model (ExponentialModel): The model containing the parameters for
                                            generating the exponential data.

    Yields:
        str: A string representation of a data point in the exponential distribution.
    """
    while True:
        try:
            data_point = expon.rvs(scale=exponential_model.scale)
            yield f"{data_point:.3f}\n"
            await asyncio.sleep(exponential_model.interval)
        except ValueError as value_error:
            logger.error(
                "Value error occurred while generating exponential distribution: %s",
                value_error,
            )
            continue
        except asyncio.CancelledError:
            logger.info("Exponential distribution data generation was cancelled.")
            break
        except Exception as error:
            logger.exception(
                "An unexpected error occurred while generating exponential distribution data: %s",
                error,
            )
            raise
