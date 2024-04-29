"""
Main module for the Streaming Data Generator application.
"""

import logging
import os
import sys
import uvicorn
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from app.endpoints.endpoints import router as api_router


# Configure logging
log_file_path = os.path.join(base_dir, "app.log")
config_path = os.path.join(base_dir, "logging.conf")

logging.config.fileConfig(
    config_path, defaults={"logfilename": log_file_path}, disable_existing_loggers=True
)
logger = logging.getLogger(__name__)

# Create a FastAPI instance
app = FastAPI()
app.include_router(api_router)


# Exception handler for general exceptions
@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    """
    Exception handler for general exceptions.
    """
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"message": "An unexpected error occurred"},
    )


logger.info("Starting the Streaming Data Generator")

# Start the FastAPI server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
