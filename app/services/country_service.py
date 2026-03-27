"""Country service for business logic"""

from app.repositories import CountryRepository


class CountryService:
    """Service for country-related operations"""

    def __init__(self, repo: CountryRepository) -> None:
        self._repo = repo

    def get_all_countries(self) -> list[str]:
        return self._repo.get_all()
