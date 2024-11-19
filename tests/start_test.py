import pytest
from httpx import AsyncClient
from app.main import app


@pytest.mark.asyncio
async def test_login_for_access_token():
    """
    Test the /token endpoint for generating access tokens.
    """
    form_data = {
        "username": "admin",
        "password": "secret",
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/auth/token", data=form_data)  # Adjusted to /auth/token
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"
    assert "access_token" in response.json(), "Response does not include 'access_token'"
    assert response.json()["token_type"] == "bearer", "Token type is not 'bearer'"


@pytest.mark.asyncio
async def test_create_qr_code_unauthorized():
    """
    Test the /qr/generate endpoint without authorization to ensure security.
    """
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post('/qr/generate', json={"data": "testdata"})
    assert response.status_code == 401, f"Expected 401 Unauthorized but got {response.status_code}"


@pytest.mark.asyncio
async def test_create_qr_code_invalid_data():
    """
    Test the /qr/generate endpoint with invalid input data.
    """
    token = "mock_access_token"  # Replace with a valid token
    headers = {"Authorization": f"Bearer {token}"}

    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post('/qr/generate', json={"invalid_key": "testdata"}, headers=headers)
    assert response.status_code == 422, f"Expected 422 Unprocessable Entity but got {response.status_code}"



@pytest.mark.asyncio
async def test_create_qr_code_success():
    """
    Test the /qr/generate endpoint with valid data and proper authorization.
    """
    token = "mock_access_token"  # Replace with a valid token
    headers = {"Authorization": f"Bearer {token}"}
    qr_request = {
        "url": "https://example.com",
        "fill_color": "black",
        "back_color": "yellow",
        "size": 10
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/qr/generate", json=qr_request, headers=headers)
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"
    assert "path" in response.json(), "Response does not include 'path'"


@pytest.mark.asyncio
async def test_list_qr_codes():
    """
    Test the /qr/list endpoint to retrieve all QR codes.
    """
    token = "mock_access_token"  # Replace with a valid token
    headers = {"Authorization": f"Bearer {token}"}
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/qr/list", headers=headers)
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"
    assert isinstance(response.json(), list), "Response is not a list of QR codes"
