"""Repository interfaces and implementations for data access"""

from typing import Protocol

from app.data.countries import UN_COUNTRIES
from app.data.divisions import ADMINISTRATIVE_DIVISIONS


class CountryRepository(Protocol):
    def get_all(self) -> list[str]: ...
    def find_by_name(self, name: str) -> str | None: ...


class DivisionRepository(Protocol):
    def get_divisions(self, country_name: str) -> list[str] | None: ...


class InMemoryCountryRepository:
    def __init__(self) -> None:
        self._countries = set(UN_COUNTRIES)
        self._countries_list = UN_COUNTRIES

    def get_all(self) -> list[str]:
        return self._countries_list

    def find_by_name(self, name: str) -> str | None:
        return name if name in self._countries else None


class InMemoryDivisionRepository:
    def __init__(self) -> None:
        self._divisions = ADMINISTRATIVE_DIVISIONS

    def get_divisions(self, country_name: str) -> list[str] | None:
        return self._divisions.get(country_name)
