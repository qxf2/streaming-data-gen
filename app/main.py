"""
Main module for the Streaming Data Generator application.
"""
import os
import sys
import logging

import uvicorn
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi import (
    FastAPI,
    Request,
    status,
)
from fastapi.exceptions import RequestValidationError
from fastapi.responses import (
    FileResponse,
    JSONResponse,
)
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder

# Import from local modules
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from app.endpoints.endpoints import router as api_router
from app.endpoints.anomaly_endpoints import router as anomaly_api_router
from app.endpoints.auth_endpoint import router as auth_router
from logging_config import setup_logging

from app.db_utils.database import Base, engine

# Configure the root logger using setup_logging function
setup_logging()

# Create a FastAPI instance
app = FastAPI()

origins = ["http://localhost", "http://localhost:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logger = logging.getLogger(__name__)

app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/")
async def serve_main_page():
    """
    Serves the main page of the Data Stream Generator App.
    """
    return FileResponse("app/static/index.html")

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """
    Handle exceptions related to request validation errors.
    """
    logger.error("Validation error occurred: %s", exc.errors())
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()}),
    )

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    """
    Handle exceptions related to HTTP errors.
    """
    logger.error("HTTP error occurred: %s", {exc.detail})
    return JSONResponse(
        status_code=exc.status_code,
        content=jsonable_encoder({"detail": exc.detail}),
    )

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    """
    Handle all other excetions that are not explicitly handled by other exception handlers.
    """
    logger.error("An exception occurred: %s", exc)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=jsonable_encoder({"detail": "Internal server error"}),
    )

app.include_router(api_router)
app.include_router(anomaly_api_router, prefix="/anomalies")
app.include_router(auth_router)

Base.metadata.create_all(bind=engine)

logger.info("Starting the Streaming Data Generator")

# Start the FastAPI server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
