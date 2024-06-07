"""
This script defines Pydantic models representing various anomaly models.
"""
from pydantic import BaseModel, Field

class RandomAnomalyModel(BaseModel):
    """
    A model representing the parameters for generating random anomalies.
    """
    base_value: float = Field(
        default=0.0,
        title="Base Value",
        description="The constant value for regular data points.",
    )
    anomaly_probability: float = Field(
        default=0.05,
        title="Anomaly Probability",
        description="The probability of an anomaly occurring at each data point.",
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


class RandomSquareModel(BaseModel):
    """
    A model representing the parameters for generating random positive square wave anomalies.
    """
    base_value: float = Field(
        default=0.0,
        title="Constant Value",
        description="The constant value for regular data points.",
    )
    anomaly_magnitude: float = Field(
        default=20.0,
        title="Anomaly Magnitude",
        description="The magnitude of the anomaly to add to the base value",
    )
    minimum_interval: float = Field(
        default=50.0,
        title="Minimum Interval",
        description="The minimum interval between wave of anomalies",
    )
    maximum_interval: float = Field(
        default=150.0,
        title="Maximum Interval",
        description="The maximum interval between wave of anomalies",
    )
    min_anomaly_duration: float = Field(
        default=5.0,
        title="Minimum Anomaly Duration",
        description="The minimum length of the wave",
    )
    max_anomaly_duration: float = Field(
        default=10.0,
        title="Maximum Anomaly Duration",
        description="The maximum length of the wave",
    )
    data_interval: float = Field(
        default=1.0,
        title="Interval",
        description="The rate at which data points are generated.",
    )


class ClusteredAnomalyModel(BaseModel):
    """
    A model representing the parameters for generating clustered anomalies.
    """
    constant_value: float = Field(
        default=0.0,
        title="Constant Value",
        description="The constant value for regular data points.",
    )
    anomaly_magnitude: float = Field(
        default=10.0,
        title="Anomaly Magnitude",
        description="The magnitude of the anomaly to add to the base value",
    )
    minimum_interval: float = Field(
        default=50.0,
        title="Minimum Interval",
        description="The minimum interval between cluster of anomalies",
    )
    maximum_interval: float = Field(
        default=150.0,
        title="Maximum Interval",
        description="The maximum interval between cluster of anomalies",
    )
    min_anomaly_length: float = Field(
        default=5.0,
        title="Minimum Anomaly Length",
        description="The minimum length of the anomalies in the cluster",
    )
    max_anomaly_length: float = Field(
        default=10.0,
        title="Maximum Anomaly Length",
        description="The maximum length of the anomalies in the cluster",
    )
    data_interval: float = Field(
        default=1.0,
        title="Interval",
        description="The rate at which data points are generated.",
    )

class SpikeAnomalyModel(BaseModel):
    """
    A model representing the parameters for generating spiked anomalies at regular intervals.
    """
    base_value: float = Field(
        default=0.0,
        title="Base Value",
        description="The constant value for regular data points.",
    )
    spike_interval: int = Field(
        default=20.0,  # change this. it should be in seconds. 20 * 60
        title="Spike Interval",
        description="The interval in seconds at which anomaly spike should occur.",
    )
    min_spike_range: float = Field(
        default=5.0,
        title="Minimum Spike Range",
        description="The minimum range for the spike values.",
    )
    max_spike_range: float = Field(
        default=10.0,
        title="Maximum Spike Range",
        description="The maximum range for the spike values.",
    )
    data_interval: float = Field(
        default=1.0,
        title="Interval",
        description="The rate at which data points are generated.",
    )

class CountBasedAnomalyModel(BaseModel):
    """
    A model representing the parameters for generating specified number of anomalies within 1 hour.
    """
    base_value: float = Field(
        default=0.0,
        title="Base Value",
        description="The constant value for regular data points.",
    )
    num_anomalies: int = Field(
        default=1,
        title="Anomaly Count",
        description="The number of anomalies to introduce within the duration.",
    )
    min_anomaly_range: float = Field(
        default=-10.0,
        title="Minimum Anomaly Range",
        description="The minimum range for the anomaly values.",
    )
    max_anomaly_range: float = Field(
        default=10.0,
        title="Maximum Anomaly Range",
        description="The maximum range for the anomaly values.",
    )
    data_interval: float = Field(
        default=1.0,
        title="Interval",
        description="The rate at which data points are generated.",
    )
