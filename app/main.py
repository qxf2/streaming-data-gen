"""
Main module for the Streaming Data Generator application.
"""

import logging
import os
import sys
import uvicorn
from fastapi import FastAPI, Request, status, HTTPException
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse, JSONResponse

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from app.endpoints.endpoints import router as api_router

# Create a FastAPI instance
app = FastAPI()

# Configure logging
log_file_path = os.path.join(base_dir, "app.log")
config_path = os.path.join(base_dir, "logging.conf")

logging.config.fileConfig(
    config_path, defaults={"logfilename": log_file_path}, disable_existing_loggers=True
)
logger = logging.getLogger(__name__)


# Custom exception handler for request validation errors
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = "\n".join([f"{e['loc'][1]}: {e['msg']}" for e in exc.errors()])
    return PlainTextResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=f"Validation error:\n{errors}",
    )

# Custom exception handler for HTTP exceptions
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return PlainTextResponse(
        status_code=exc.status_code,
        content=f"HTTP error: {exc.detail}",
    )

# General exception handler for all other exceptions
@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    return PlainTextResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content="An internal server error occurred.",
    )

app.include_router(api_router)

logger.info("Starting the Streaming Data Generator")

# Start the FastAPI server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
