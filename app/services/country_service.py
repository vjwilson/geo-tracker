"""Country service for business logic"""

from app.data.countries import UN_COUNTRIES
from app.utils.text import decode_country_name


class CountryService:
    """Service for country-related operations"""

    def get_all_countries(self) -> list[str]:
        """Get list of all UN-recognized countries

        Returns:
            List of country names
        """
        return UN_COUNTRIES

    def find_country(self, country_name: str) -> str | None:
        """Find a country by URL-encoded name

        Args:
            country_name: URL-encoded country name (e.g., "united-states")

        Returns:
            Country name if found, None otherwise
        """
        decoded_name = decode_country_name(country_name)
        return decoded_name if decoded_name in UN_COUNTRIES else None


# Singleton instance
country_service = CountryService()
