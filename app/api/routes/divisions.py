"""Administrative division routes"""

from fastapi import APIRouter, HTTPException

from app.services.division_service import division_service

router = APIRouter(prefix="/countries", tags=["divisions"])


@router.get("/{country_name}/administrative-divisions")
def get_administrative_divisions(country_name: str) -> list[str] | str:
    """Get administrative divisions for a country

    Args:
        country_name: URL-encoded country name (e.g., "united-states")

    Returns:
        List of divisions if available, or "Not Implemented Yet" if country exists but no data

    Raises:
        HTTPException: 404 if country not found
    """
    country_exists, result = division_service.get_divisions(country_name)

    if not country_exists:
        raise HTTPException(status_code=404, detail="Country not found")

    return result
