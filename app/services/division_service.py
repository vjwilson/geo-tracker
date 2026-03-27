"""Administrative division service for business logic"""

from app.repositories import CountryRepository, DivisionRepository


class DivisionService:
    """Service for administrative division operations"""

    def __init__(
        self, country_repo: CountryRepository, division_repo: DivisionRepository
    ) -> None:
        self._country_repo = country_repo
        self._division_repo = division_repo

    def get_divisions(self, country_name: str) -> list[str] | str:
        """Get administrative divisions for a verified country.

        Args:
            country_name: Already-resolved country name (e.g., "United States")

        Returns:
            List of divisions if available, or "Not Implemented Yet"
        """
        divisions = self._division_repo.get_divisions(country_name)
        if divisions is not None:
            return divisions
        return "Not Implemented Yet"
