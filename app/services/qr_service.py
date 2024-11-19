import os
from typing import List
import qrcode
import logging
from pathlib import Path
from app.config import SERVER_BASE_URL, SERVER_DOWNLOAD_FOLDER, QR_DIRECTORY


def ensure_qr_directory_exists():
    """
    Ensures that the QR_DIRECTORY exists. Creates the directory if it does not exist.
    """
    if not QR_DIRECTORY.exists():
        logging.info(f"Directory {QR_DIRECTORY} not found. Creating it.")
        QR_DIRECTORY.mkdir(parents=True, exist_ok=True)


def list_qr_codes(directory_path: Path = QR_DIRECTORY) -> List[str]:
    """
    Lists all QR code images in the specified directory by returning their filenames.
    Parameters:
    - directory_path (Path): The filesystem path to the directory containing QR code images.

    Returns:
    - A list of filenames (str) for QR codes found in the directory.
    """
    try:
        # Ensure the directory exists before attempting to list files
        ensure_qr_directory_exists()

        # Filter files ending with .png and return as a list
        qr_files = [
            file.name
            for file in directory_path.iterdir()
            if file.is_file() and file.suffix == ".png"
        ]

        logging.info(f"Found {len(qr_files)} QR code(s) in directory {directory_path}.")
        return qr_files
    except Exception as e:
        # Log any unexpected errors
        logging.error(f"Error accessing directory {directory_path}: {e}")
        return []


def generate_qr_code(
    data: str, fill_color: str = "black", back_color: str = "white", size: int = 10
) -> str:
    """
    Generates a QR code based on the provided data and saves it to the QR_DIRECTORY.
    Parameters:
    - data (str): The data to encode in the QR code.
    - fill_color (str): The fill color for the QR code.
    - back_color (str): The background color for the QR code.
    - size (int): The size of the QR code (default: 10).

    Returns:
    - The path to the generated QR code file.
    """
    try:
        ensure_qr_directory_exists()

        # Convert data to string if it is not already
        if not isinstance(data, str):
            data = str(data)

        # Sanitize and generate filename
        sanitized_data = data.replace(" ", "_").replace("/", "_")
        filename = f"{sanitized_data}.png"
        file_path = QR_DIRECTORY / filename

        # Create the QR code
        qr = qrcode.QRCode(
            version=size,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color=fill_color, back_color=back_color)

        # Convert file_path to string before saving
        img.save(str(file_path))

        logging.info(f"QR Code generated successfully: {file_path}")
        return str(file_path)

    except Exception as e:
        logging.error(f"Failed to generate QR code: {e}")
        raise


def delete_qr_code(filename: str) -> bool:
    """
    Deletes a QR code file from the QR_DIRECTORY.
    Parameters:
    - filename (str): The name of the QR code file to delete.

    Returns:
    - True if the file was successfully deleted, False otherwise.
    """
    try:
        file_path = QR_DIRECTORY / filename
        if file_path.exists():
            file_path.unlink()
            logging.info(f"Deleted QR code file: {file_path}")
            return True
        else:
            logging.warning(f"File not found for deletion: {file_path}")
            return False
    except Exception as e:
        logging.error(f"Failed to delete QR code file {filename}: {e}")
        return False
