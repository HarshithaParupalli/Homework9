from fastapi import FastAPI
from app.config import QR_DIRECTORY
from app.routers import qr_code, oauth
from app.services.qr_service import ensure_qr_directory_exists
from app.utils.common import setup_logging

# This function sets up logging based on the configuration specified in your logging configuration file.
# It's important for monitoring and debugging.
setup_logging()

# This ensures that the directory for storing QR codes exists when the application starts.
# If it doesn't exist, it will be created.
ensure_qr_directory_exists()

# This creates an instance of the FastAPI application.
app = FastAPI(
    title="QR Code Manager",
    description="A FastAPI application for creating, listing, and deleting QR codes. "
    "It also supports OAuth for secure access.",
    version="0.0.1",
)

# Include routers for API endpoints.
# The qr_code router handles QR code operations, and the oauth router handles authentication.
app.include_router(qr_code.router, prefix="/qr", tags=["QR Codes"])
app.include_router(oauth.router, prefix="/auth", tags=["Authentication"])


# Define a root endpoint for basic connectivity testing.
@app.get("/")
async def read_root():
    """
    A simple root endpoint to test connectivity.
    Returns a welcome message.
    """
    return {"message": "Welcome to the QR Code Manager API"}
