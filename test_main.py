import pytest
from fastapi.testclient import TestClient
from main import app, UN_COUNTRIES, ADMINISTRATIVE_DIVISIONS

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


def test_get_country_simple():
    """Test getting a single-word country"""
    response = client.get("/countries/canada")
    assert response.status_code == 200
    assert response.json() == "Canada"


def test_get_country_multi_word():
    """Test getting a multi-word country with hyphens"""
    response = client.get("/countries/united-states")
    assert response.status_code == 200
    assert response.json() == "United States"


def test_get_country_complex_name():
    """Test getting a country with a complex multi-word name"""
    response = client.get("/countries/new-zealand")
    assert response.status_code == 200
    assert response.json() == "New Zealand"


def test_get_country_case_insensitive():
    """Test that country lookup handles different cases"""
    response = client.get("/countries/UNITED-KINGDOM")
    assert response.status_code == 200
    assert response.json() == "United Kingdom"


def test_get_country_not_found():
    """Test that non-existent country returns 'Country Not Found'"""
    response = client.get("/countries/atlantis")
    assert response.status_code == 200
    assert response.json() == "Country Not Found"


def test_get_country_not_found_multi_word():
    """Test that non-existent multi-word country returns 'Country Not Found'"""
    response = client.get("/countries/made-up-country")
    assert response.status_code == 200
    assert response.json() == "Country Not Found"


def test_get_country_with_and():
    """Test getting a country with 'and' in the name"""
    response = client.get("/countries/antigua-and-barbuda")
    assert response.status_code == 200
    assert response.json() == "Antigua and Barbuda"


def test_get_country_with_and_and_the():
    """Test getting a country with both 'and' and 'the' in the name"""
    response = client.get("/countries/saint-vincent-and-the-grenadines")
    assert response.status_code == 200
    assert response.json() == "Saint Vincent and the Grenadines"


def test_get_country_with_of():
    """Test getting a country with 'of' in the name"""
    response = client.get("/countries/democratic-republic-of-the-congo")
    assert response.status_code == 200
    assert response.json() == "Democratic Republic of the Congo"


def test_get_administrative_divisions_united_states():
    """Test getting administrative divisions for United States"""
    response = client.get("/countries/united-states/administrative-divisions")
    assert response.status_code == 200
    divisions = response.json()
    assert isinstance(divisions, list)
    assert "California" in divisions
    assert "Texas" in divisions
    assert "New York" in divisions
    assert len(divisions) == 56  # 50 states + DC + 5 territories


def test_get_administrative_divisions_canada():
    """Test getting administrative divisions for Canada"""
    response = client.get("/countries/canada/administrative-divisions")
    assert response.status_code == 200
    divisions = response.json()
    assert isinstance(divisions, list)
    assert "Ontario" in divisions
    assert "Quebec" in divisions
    assert "British Columbia" in divisions
    assert len(divisions) == 13  # 10 provinces + 3 territories


def test_get_administrative_divisions_not_implemented():
    """Test that other known countries return 'Not Implemented Yet'"""
    response = client.get("/countries/france/administrative-divisions")
    assert response.status_code == 200
    assert response.json() == "Not Implemented Yet"


def test_get_administrative_divisions_country_not_found():
    """Test that unknown countries return 'Country Not Found'"""
    response = client.get("/countries/atlantis/administrative-divisions")
    assert response.status_code == 200
    assert response.json() == "Country Not Found"


def test_get_administrative_divisions_matches_lookup_table():
    """Test that endpoint returns data matching the lookup table"""
    response = client.get("/countries/united-states/administrative-divisions")
    assert response.json() == ADMINISTRATIVE_DIVISIONS["United States"]


def test_invalid_endpoint():
    """Test that invalid endpoints return 404"""
    response = client.get("/invalid")
    assert response.status_code == 404
