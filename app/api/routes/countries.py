"""Country routes"""

from typing import Annotated

from fastapi import APIRouter, Depends

from app.dependencies import get_country_service, resolve_country
from app.services.country_service import CountryService

router = APIRouter(prefix="/countries", tags=["countries"])


@router.get("/")
def list_countries(
    service: Annotated[CountryService, Depends(get_country_service)],
) -> list[str]:
    return service.get_all_countries()


@router.get("/{country_name}")
def get_country(
    country: Annotated[str, Depends(resolve_country)],
) -> str:
    return country
