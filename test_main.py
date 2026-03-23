import pytest
from fastapi.testclient import TestClient
from main import app, UN_COUNTRIES

client = TestClient(app)


def test_root_endpoint():
    """Test that root endpoint returns 'Hello'"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Hello"


def test_root_endpoint_content_type():
    """Test that root endpoint returns JSON content type"""
    response = client.get("/")
    assert response.headers["content-type"] == "application/json"


def test_countries_endpoint():
    """Test that countries endpoint returns list of countries"""
    response = client.get("/countries")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_countries_endpoint_count():
    """Test that countries endpoint returns correct number of countries"""
    response = client.get("/countries")
    countries = response.json()
    assert len(countries) == 193


def test_countries_endpoint_contains_expected_countries():
    """Test that countries endpoint contains specific known countries"""
    response = client.get("/countries")
    countries = response.json()

    # Check a few well-known countries
    assert "United States" in countries
    assert "Canada" in countries
    assert "United Kingdom" in countries
    assert "Japan" in countries


def test_countries_endpoint_matches_constant():
    """Test that countries endpoint returns the same data as UN_COUNTRIES constant"""
    response = client.get("/countries")
    assert response.json() == UN_COUNTRIES


def test_invalid_endpoint():
    """Test that invalid endpoints return 404"""
    response = client.get("/invalid")
    assert response.status_code == 404
