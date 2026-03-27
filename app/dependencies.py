"""FastAPI dependency injection functions"""

from typing import Annotated

from fastapi import Depends, HTTPException

from app.repositories import (
    CountryRepository,
    DivisionRepository,
    InMemoryCountryRepository,
    InMemoryDivisionRepository,
)
from app.services.country_service import CountryService
from app.services.division_service import DivisionService
from app.utils.text import decode_country_name


def get_country_repo() -> CountryRepository:
    return InMemoryCountryRepository()


def get_division_repo() -> DivisionRepository:
    return InMemoryDivisionRepository()


def get_country_service(
    repo: Annotated[CountryRepository, Depends(get_country_repo)],
) -> CountryService:
    return CountryService(repo)


def get_division_service(
    country_repo: Annotated[CountryRepository, Depends(get_country_repo)],
    division_repo: Annotated[DivisionRepository, Depends(get_division_repo)],
) -> DivisionService:
    return DivisionService(country_repo, division_repo)


def resolve_country(
    country_name: str,
    repo: Annotated[CountryRepository, Depends(get_country_repo)],
) -> str:
    """Decode a URL slug and verify the country exists. Raises 404 if not found."""
    decoded = decode_country_name(country_name)
    country = repo.find_by_name(decoded)
    if country is None:
        raise HTTPException(status_code=404, detail="Country not found")
    return country
