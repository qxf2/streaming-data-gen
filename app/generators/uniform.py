"""
Module for generating an uniform distribution data stream based on
the given UniformModel parameters.
"""

import asyncio
import logging
from scipy.stats import uniform
from app.models.distribution_models import UniformModel

logger = logging.getLogger(__name__)


async def generate_uniform_data(uniform_model: UniformModel):
    """
    Generates a uniform distribution data based on the provided Uniform model parameters.

    Args:
        uniform_model (UniformModel): The model containing the parameters for
                                        generating the uniform data.

    Yields:
        str: A string representation of a data point in the uniform distribution.
    """
    while True:
        try:
            data_point = uniform.rvs(
                loc=uniform_model.min_val,
                scale=uniform_model.max_val - uniform_model.min_val,
            )
            yield f"{data_point:.3f}\n"
            await asyncio.sleep(uniform_model.interval)
        except ValueError as value_error:
            logger.error(
                "Value error occurred while generating uniform distribution: %s",
                value_error,
            )
            continue
        except asyncio.CancelledError:
            logger.info("Uniform distribution data generation was cancelled.")
            break
        except Exception as error:
            logger.exception(
                "An unexpected error occurred while generating uniform distribution data: %s",
                error,
            )
            raise
