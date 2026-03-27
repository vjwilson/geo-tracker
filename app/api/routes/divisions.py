"""Administrative division routes"""

from typing import Annotated

from fastapi import APIRouter, Depends

from app.dependencies import get_division_service, resolve_country
from app.services.division_service import DivisionService

router = APIRouter(prefix="/countries", tags=["divisions"])


@router.get("/{country_name}/administrative-divisions")
def get_administrative_divisions(
    country: Annotated[str, Depends(resolve_country)],
    service: Annotated[DivisionService, Depends(get_division_service)],
) -> list[str] | str:
    return service.get_divisions(country)
