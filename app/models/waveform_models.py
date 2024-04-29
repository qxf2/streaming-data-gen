"""
This script defines Pydantic models representing various waveforms.
"""

from pydantic import BaseModel, Field


class SineModel(BaseModel):
    """
    A model representing a sine wave.
    """
    amplitude: float = Field(
        default=4, description="The distance from height of a peak to center line."
    )
    frequency: float = Field(
        default=2,
        description="The number of cycles per second of the sine wave (in Hertz).",
    )
    phase: int = Field(
        default=0, description="The offset of the sine wave (in degrees)."
    )
    sample_rate: int = Field(
        default=100,
        description="The frequency of generated data points in samples per second.",
    )
    interval: float = Field(
        default=1.0, description="The time interval between data points (in seconds)."
    )


class CosineModel(BaseModel):
    """
    A model representing a cosine wave.
    """

    amplitude: float = Field(
        default=4, description="The distance from height of a peak to center line."
    )
    frequency: float = Field(
        default=2,
        description="The number of cycles per second of the cosine wave (in Hertz).",
    )
    phase: int = Field(
        default=0, description="The offset of the cosine wave (in degrees)."
    )
    sample_rate: int = Field(
        default=100,
        description="The frequency of generated data points in samples per second.",
    )
    interval: float = Field(
        default=1.0, description="The time interval between data points (in seconds)."
    )


class SquareModel(BaseModel):
    """
    A model representing a square wave.
    """

    frequency: float = Field(
        default=2.0,
        description="The number of cycles per second of the square wave (in Hertz).",
    )
    sample_rate: int = Field(
        default=100,
        description="The frequency of generated data points in samples per second.",
    )
    interval: float = Field(
        default=1.0, description="The time interval between data points (in seconds)."
    )


class SawtoothModel(BaseModel):
    """
    A model representing a sawtooth wave.
    """

    amplitude: float = Field(
        default=1.0,
        title="Amplitude",
        description="The distance from height of a peak to center line.",
    )
    frequency: float = Field(
        default=2.0,
        title="Frequency",
        description="The number of cycles per second of the sawtooth wave (in Hertz).",
    )
    sample_rate: int = Field(
        default=100,
        title="Sample Rate",
        description="The frequency of generated data points in samples per second.",
    )
    interval: float = Field(
        default=1.0,
        title="Interval",
        description="The time interval between data points (in seconds).",
    )
