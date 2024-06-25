"""
Module for defining FastAPI endpoints that generates data with anomalies.

Endpoints:
    /random: Endpoint for generating data with random anomalies
    /random-square: Endpoint for generating data with random square wave anomalies
    /clustered: Endpoint for generating data with clustered anomalies
    /periodic-spike: Endpoint for generating data with periodic spike anomalies
        within 1 hour duration
    /count-per-duration: Endopint for generating data with specified 
        number of anomalies within 1 hour duration

"""

import logging
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from app.generators.anomalies import (
    periodic_spike,
    clustered,
    count_duration,
    random_anomaly,
    random_square,
)
from app.db_utils.crud import verify_token
from app.models.auth_model import TokenData

router = APIRouter()

logger = logging.getLogger(__name__)


@router.get("/random", response_class=StreamingResponse)
async def generate_random_anomaly(
    random_anomaly_model: random_anomaly.RandomAnomalyModel = Depends(),
    token_data: TokenData = Depends(verify_token),
):
    """
    Generate streaming data with random anomalies.

    Parameters:
    - random_anomaly: An instance of the RandomAnomalyModel class defining the parameters
    of the data to be generated. If not provided, default parameters will be used.
    The parameters include:
        - base_value (float): The constant value for regular data points.
        - anomaly_probability(float): The probability of an anomaly occurring
        - anomaly_range(float): The range within which the anomaly values can vary
        - data_interval(float): The time interval between data points

    Returns:
    - StreamingResponse: A streaming response containing the generated data with anomalies.
    """
    try:
        logger.info(
            "Generating data with random anomalies for user '%s' with parameters: %s",
            token_data.username,
            random_anomaly_model,
        )
        return StreamingResponse(
            random_anomaly.generate_random_anomalies(random_anomaly_model),
            media_type="text/event-stream",
        )
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error)) from error


@router.get("/random-square", response_class=StreamingResponse)
async def random_square_anomaly(
    pos_square: random_square.RandomSquareModel = Depends(),
    token_data: TokenData = Depends(verify_token),
):
    """
    Generate streaming data with random square wave anomalies.

    Parameters:
    - pos_square: An instance of the RandomSquareModel class defining the parameters
    of the data to be generated. If not provided, default parameters will be used.
    The parameters include:
        - base_value (float): The constant value for regular data points.
        - anomaly_magnitude (float): The magnitude of the anomaly to add to the base value.
        - min_anomaly_duration (int): The minimum duration of the anomaly in data points.
        - max_anomaly_duration (int): The maximum duration of the anomaly in data points.
        - data_interval (float): The time interval between data points in seconds.

    Returns:
    - StreamingResponse: A streaming response containing the generated data with anomalies.
    """
    try:
        logger.info(
            "Generating data with random square wave anomalies for user '%s' with parameters: %s",
            token_data.username,
            pos_square,
        )
        return StreamingResponse(
            random_square.generate_random_square(pos_square),
            media_type="text/event-stream",
        )
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error)) from error


@router.get("/clustered", response_class=StreamingResponse)
async def generate_clustered_anomaly(
    clustered_anomaly: clustered.ClusteredAnomalyModel = Depends(),
    token_data: TokenData = Depends(verify_token),
):
    """
    Generate streaming data with clustered anomalies.

    Parameters:
    - clustered_anomaly: An instance of the ClusteredAnomalyModel class defining the parameters
    of the data to be generated. If not provided, default parameters will be used.
    The parameters include:
        - constant_value (float): The base or constant value for regular data points.
        - anomaly_magnitude (float): The magnitude of the anomalies.
        - anomaly_interval_range (float):
            minimum and maximum interval between clusters of anomalies
        - anomaly_length_range (float):
            The minimum and maximum length of a cluster of anomalies.
        - data_interval (float): The time interval between data points.

    Returns:
        - StreamingResponse: A streaming response containing the generated data with anomalies.
    """
    try:
        logger.info(
            "Generating data with clustered anomalies for user '%s' with parameters: %s",
            token_data.username,
            clustered_anomaly,
        )
        return StreamingResponse(
            clustered.generate_clustered_anomalies(clustered_anomaly),
            media_type="text/event-stream",
        )
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error)) from error


@router.get("/periodic-spike", response_class=StreamingResponse)
async def generate_spike_anomaly(
    spike_anomaly: periodic_spike.SpikeAnomalyModel = Depends(),
    token_data: TokenData = Depends(verify_token),
):
    """
    Generate streaming data with regular spikes occurring at
    specified interval within a duration of 1 hour.

    Parameters:
    - spike_anomaly: An instance of the SpikeAnomalyModel class defining the parameters
    of the data to be generated. If not provided, default parameters will be used.
    The parameters include:
        - base_value (float): The base or constant value around which anomalies will occur.
        - spike_interval (int): The interval in seconds at which spikes should occur.
        - spike_range (tuple): The range (lower and upper bounds) for the spike values.
        - data_interval (float): The time interval between data points.

    Returns:
        - StreamingResponse: A streaming response containing the generated data with anomalies.
    """
    try:
        logger.info(
            "Generating data with periodic spike anomalies for user '%s' with parameters: %s",
            token_data.username,
            spike_anomaly,
        )
        return StreamingResponse(
            periodic_spike.generate_periodic_spike_data(spike_anomaly),
            media_type="text/event-stream",
        )
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error)) from error


@router.get("/count-per-duration", response_class=StreamingResponse)
async def count_per_duration(
    count_based: count_duration.CountBasedAnomalyModel = Depends(),
    token_data: TokenData = Depends(verify_token),
):
    """
    Generate streaming data with specified number of anomalies within a duration of 1 hour.

    Parameters:
    - count_based: An instance of the CountBasedAnomalyModel class defining the parameters
    of the data to be generated. If not provided, default parameters will be used.
    The parameters include:
        - base_value (float): The base or constant value around which anomalies will occur.
        - num_anomalies (int): The number of anomalies to introduce within the duration.
        - anomaly_range (tuple): The range (lower and upper bounds) for the anomaly values.
        - data_interval (float): The rate at which data points are generated.

    Returns:
        - StreamingResponse: A streaming response containing the generated data with anomalies.
    """
    try:
        logger.info(
            "Generating data with count based anomalies for user '%s' with parameters: %s",
            token_data.username,
            count_based,
        )
        return StreamingResponse(
            count_duration.generate_count_based_anomalies_data(count_based),
            media_type="text/event-stream",
        )
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error)) from error
