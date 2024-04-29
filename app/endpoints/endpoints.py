"""
Module for defining FastAPI endpoints.

Endpoints:
    /sine: Endpoint for generating a sine wave.
    /cosine: Endpoint for generating a cosine wave.
    /sawtooth: Endpoint for generating a sawtooth wave.
    /square: Endpoint for generating a square wave.
    /normal: Endpoint for generating a normal distribution.
    /uniform: Endpoint for generating a uniform distribution.
    /exponential: Endpoint for generating an exponential distribution.
"""

import logging
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from app.generators import sine, cosine, square, sawtooth, normal, uniform, exponential
from app.anomalies.anomaly_manager import AnomalyManager
from app.models.anomaly_models import RandomAnomalyParameters

router = APIRouter()

logger = logging.getLogger(__name__)


@router.get("/sine", response_class=StreamingResponse)
async def sine_wave(sine_model: sine.SineModel = Depends()):
    """
    Generate a streaming sine wave.

    Parameters:
    - sine_model: An instance of the SineModel class defining the parameters
    of the sine wave to be generated. If not provided, default parameters will be used.
    The parameters include:
        - amplitude (float): The distance from height of a peak to center line.
        - frequency (float): The number of cycles per second of the sine wave (in Hertz).
        - phase (int): The offset of the sine wave (in degrees).
        - sample_rate (int): The frequency of generated data points in samples per second.
        - interval (float): The time interval between data points (in seconds).

    Returns:
    - StreamingResponse: A streaming response containing the generated sine wave data.
    """
    logger.info("Generating sine wave with parameters: %s", sine_model)
    return StreamingResponse(
        sine.generate_sine_data(sine_model), media_type="text/event-stream"
    )


@router.get("/cosine", response_class=StreamingResponse)
async def cosine_wave(cosine_model: cosine.CosineModel = Depends()):
    """
    Generate a streaming cosine wave.

    Parameters:
    - cosine_model: An instance of the CosineModel class defining the parameters
      of the cosine wave to be generated. If not provided, default parameters will be used.
      The parameters include:
        - amplitude (float): The distance from height of a peak to center line.
        - frequency (float): The number of cycles per second of the cosine wave (in Hertz).
        - phase (int): The offset of the cosine wave (in degrees).
        - sample_rate (int): The frequency of generated data points in samples per second.
        - interval (float): The time interval between data points in seconds.

    Returns:
    - StreamingResponse: A streaming response containing the generated cosine wave data.
    """
    logger.info("Generating cosine wave with parameters: %s", cosine_model)
    return StreamingResponse(
        cosine.generate_cosine_data(cosine_model), media_type="text/event-stream"
    )


@router.get("/sawtooth", response_class=StreamingResponse)
async def sawtooth_wave(sawtooth_model: sawtooth.SawtoothModel = Depends()):
    """
    Generate a streaming sawtooth wave.

    Parameters:
    - sawtooth_model : An instance of the SawtoothModel class defining the parameters
      of the sawtooth wave to be generated. If not provided, default parameters will be used.
      The parameters include:
        - amplitude (float): The distance from height of a peak to center line.
        - frequency (float): The number of cycles per second of the sawtooth wave (in Hertz).
        - sample_rate (int): The frequency of generated data points in samples per second.
        - interval (float): The time interval between data points (in seconds).

    Returns:
    - StreamingResponse: A streaming response containing the generated sawtooth wave data.
    """
    logger.info("Generating sawtooth wave with parameters: %s", sawtooth_model)
    return StreamingResponse(
        sawtooth.generate_sawtooth_data(sawtooth_model), media_type="text/event-stream"
    )


@router.get("/square", response_class=StreamingResponse)
async def square_wave(square_model: square.SquareModel = Depends()):
    """
    Generate a streaming square wave.

    Parameters:
    - square_model: An instance of the SquareModel class defining the parameters
      of the square wave to be generated. If not provided, default parameters will be used.
      The parameters include:
        - frequency (float): The number of cycles per second of the square wave (in Hertz).
        - sample_rate (int): The frequency of generated data points in samples per second.
        - interval (float): The time interval between data points (in seconds).

    Returns:
    - StreamingResponse: A streaming response containing the generated square wave data.
    """
    logger.info("Generating square wave with parameters: %s", square_model)
    return StreamingResponse(
        square.generate_square_data(square_model), media_type="text/event-stream"
    )


@router.get("/normal", response_class=StreamingResponse)
async def normal_wave(normal_model: normal.NormalModel = Depends()):
    """
    Generate a streaming normal distribution.

    Parameters:
    - normal_model: An instance of the NormalModel class defining the parameters
      of the normal distribution to be generated. If not provided, default parameters will be used.
      The parameters include:
        - mean (float): The mean of the normal distribution.
        - std_dev (float): The standard deviation of the normal distribution.
        - interval (float): The time interval between data points in seconds.

    Returns:
    - StreamingResponse: A streaming response containing the generated normal distribution data.
    """
    logger.info("Generating normal distribution with parameters: %s", normal_model)
    return StreamingResponse(
        normal.generate_normal_data(normal_model), media_type="text/event-stream"
    )


@router.get("/uniform", response_class=StreamingResponse)
async def uniform_wave(uniform_model: uniform.UniformModel = Depends()):
    """
    Generate a streaming uniform distribution.

    Parameters:
    - uniform_model: An instance of the UniformModel class defining the parameters
      of the uniform distribution to be generated. If not provided, default parameters will be used.
      The parameters include:
        - min_val (float): The minimum value of the uniform distribution.
        - max_val (float): The maximum value of the uniform distribution.
        - interval (float): The time interval between data points in seconds.

    Returns:
    - StreamingResponse: A streaming response containing the generated uniform distribution data.
    """
    logger.info("Generating uniform distribution with parameters: %s", uniform_model)
    return StreamingResponse(
        uniform.generate_uniform_data(uniform_model), media_type="text/event-stream"
    )


@router.get("/exponential", response_class=StreamingResponse)
async def exponential_wave(exponential_model: exponential.ExponentialModel = Depends()):
    """
    Generate a streaming exponential distribution.

    Parameters:
    - exponential_model: An instance of the ExponentialModel class defining the parameters
      of the exponential distribution to be generated.
      If not provided, default parameters will be used.
      The parameters include:
        - scale (float): The inverse of the rate parameter controlling
                        the rate at which events occur.
        - interval (float): The time interval between data points in seconds.

    Returns:
    - StreamingResponse: A streaming response containing the generated 
                        exponential distribution data.
    """
    logger.info("Generating exponential distribution with parameters: %s", exponential_model)
    return StreamingResponse(
        exponential.generate_exponential_data(exponential_model),
        media_type="text/event-stream",
    )


anomaly_manager = AnomalyManager()


@router.get("/anomaly/{anomaly_type}", response_class=StreamingResponse)
async def generate_anomalies(anomaly_type: str, params: RandomAnomalyParameters = Depends()):
    """
    Generates anomalies of the specified type with the provided parameters.

    Args:
        anomaly_type (str): The type of anomalies to generate.
        params : The parameters for generating the anomalies.

    Returns:
        StreamingResponse: A streaming response containing the generated anomalies.
    """
    logger.info("Generating anomalies of type: %s with parameters: %s", 
            anomaly_type, 
            params.model_dump())
    generator_function = anomaly_manager.apply_anomaly(
        anomaly_type, **params.model_dump()
    )
    if not generator_function:
        print(f"Generator function for {anomaly_type} could not be created.")
        raise HTTPException(
            status_code=400, detail=f"Invalid anomaly type: {anomaly_type}"
        )
    return StreamingResponse(generator_function(), media_type="text/event-stream")
