"""
This script defines Pydantic models representing various anomaly models.
"""

from pydantic import BaseModel, Field


class RandomAnomalyParameters(BaseModel):
    """
    A model representing the parameters for generating random anomalies.
    """
    c: float = Field(
        default=1.0,
        title="Constant Value",
        description="The constant value for regular data points.",
    )
    anomaly_probability: float = Field(
        default=0.1,
        title="Anomaly Probability",
        description="The probability of an anomaly occurring.",
    )
    anomaly_range: float = Field(
        default=5.0,
        title="Anomaly Range",
        description="The range within which the anomaly values can vary.",
    )
    data_interval: float = Field(
        default=1.0,
        title="Data Interval",
        description="The time interval between data points.",
    )


class SquareWaveAnomalyParameters(BaseModel):
    """
    A model representing the parameters for generating square wave anomalies.
    """
    c: float = Field(
        default=1.0,
        title="Constant Value",
        description="The constant value for regular data points.",
    )
    duration: int = Field(
        default=10,
        title="Duration",
        description="The duration of the square wave signal in seconds.",
    )
    interval: float = Field(
        default=1.0,
        title="Interval",
        description="The rate at which data points are generated.",
    )
