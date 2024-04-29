"""
This script defines Pydantic models representing various distributions.
"""

from pydantic import BaseModel, Field


class NormalModel(BaseModel):
    """
    A model representing a normal distribution.
    """

    mean: float = Field(
        default=0, description="The mean of the normal distribution."
    )
    std_dev: float = Field(
        default=1, description="The standard deviation of the normal distribution."
    )
    interval: float = Field(
        default=1.0, description="The time interval between data points in seconds."
    )


class UniformModel(BaseModel):
    """
    A model representing a uniform distribution.
    """

    min_val: float = Field(
        default=0, description="The minimum value of the uniform distribution."
    )
    max_val: float = Field(
        default=1, description="The maximum value of the uniform distribution."
    )
    interval: float = Field(
        default=1.0, description="The time interval between data points in seconds."
    )


class ExponentialModel(BaseModel):
    """
    A model representing an exponential distribution.
    """

    scale: float = Field(
        default=1.0,
        description="The inverse of the rate parameter controlling the rate at which events occur.",
    )
    interval: float = Field(
        default=1.0, description="The time interval between data points in seconds."
    )
