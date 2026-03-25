"""Country routes"""

from fastapi import APIRouter, HTTPException

from app.services.country_service import country_service

router = APIRouter(prefix="/countries", tags=["countries"])


@router.get("/")
def list_countries() -> list[str]:
    """Get list of all UN-recognized countries

    Returns:
        List of country names
    """
    return country_service.get_all_countries()


@router.get("/{country_name}")
def get_country(country_name: str) -> str:
    """Get a specific country by URL-encoded name

    Args:
        country_name: URL-encoded country name (e.g., "united-states")

    Returns:
        Country name if found

    Raises:
        HTTPException: 404 if country not found
    """
    country = country_service.find_country(country_name)
    if country is None:
        raise HTTPException(status_code=404, detail="Country not found")
    return country
