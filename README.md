
# **Homework9 Project**

A Python-based QR Code API designed for generating and managing QR codes with a FastAPI backend.

## **Table of Contents**
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Docker Deployment](#docker-deployment)
- [CI/CD Pipeline](#ci/cd-pipeline)
- [License](#license)

---

## **Features**
- Generate QR codes with customizable colors and sizes.
- List all generated QR codes.
- Secure authentication using JWT tokens.
- Fully tested with `pytest`.
- CI/CD pipeline for testing and deployment using GitHub Actions.
- Dockerized for containerized deployment.

---

## **Setup**

### **Local Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/HarshithaParupalli/Homework9.git
   cd Homework9
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

---

## **Usage**
Access the API at:
```
http://localhost:8000
```

To explore the available endpoints, visit the interactive Swagger documentation at:
```
http://localhost:8000/docs
```

---

## **API Endpoints**

### **Authentication**
- **POST `/auth/token`**
  - Request an access token by providing valid credentials.

### **QR Code Operations**
- **POST `/qr/generate`**
  - Generate a new QR code with customizable properties (size, color).
- **GET `/qr/list`**
  - List all generated QR codes.

### **Example Payload for `/qr/generate`**
```json
{
  "url": "https://example.com",
  "fill_color": "black",
  "back_color": "white",
  "size": 10
}
```

---

## **Testing**
Run the test suite using `pytest`:
```bash
pytest tests/
```

---

## **Docker Deployment**

### **Build and Run with Docker**
1. Build the Docker image:
   ```bash
   docker build -t qr-code-api .
   ```
2. Run the container:
   ```bash
   docker run -p 8000:8000 qr-code-api
   ```

### **Docker Compose**
1. Start services with `docker-compose`:
   ```bash
   docker-compose up --build
   ```
2. Access the application at:
   ```
   http://localhost:8000
   ```

---

## **CI/CD Pipeline**
The project includes a GitHub Actions workflow for CI/CD:
1. On every push to `main`, the pipeline:
   - Installs dependencies.
   - Runs tests.
   - Builds and pushes the Docker image to Docker Hub.
   - Deploys the application to a production server.

---

## **Project Structure**
```
Homework9/
├── app/
│   ├── main.py         # Application entry point
│   ├── routers/        # API endpoints
│   ├── services/       # Core business logic
│   ├── utils/          # Helper functions
├── tests/              # Test cases
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker configuration
├── docker-compose.yml  # Docker Compose configuration
├── start.sh            # Startup script
└── README.md           # Project documentation
```

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
