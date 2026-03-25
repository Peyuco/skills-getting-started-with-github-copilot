import pytest
from fastapi.testclient import TestClient
from src.app import app


@pytest.fixture
def client():
    """Fixture providing TestClient connected to the FastAPI app."""
    return TestClient(app)
