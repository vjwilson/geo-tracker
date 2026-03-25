"""Administrative division service for business logic"""

from app.data.countries import UN_COUNTRIES
from app.data.divisions import ADMINISTRATIVE_DIVISIONS
from app.utils.text import decode_country_name


class DivisionService:
    """Service for administrative division operations"""

    def get_divisions(self, country_name: str) -> tuple[bool, list[str] | str]:
        """Get administrative divisions for a country

        Args:
            country_name: URL-encoded country name (e.g., "united-states")

        Returns:
            Tuple of (country_exists, divisions_or_message)
            - If country doesn't exist: (False, "Country Not Found")
            - If country exists but no data: (True, "Not Implemented Yet")
            - If country exists with data: (True, [list of divisions])
        """
        decoded_name = decode_country_name(country_name)

        # Check if country exists
        if decoded_name not in UN_COUNTRIES:
            return False, "Country Not Found"

        # Check if we have divisions data
        if decoded_name in ADMINISTRATIVE_DIVISIONS:
            return True, ADMINISTRATIVE_DIVISIONS[decoded_name]
        else:
            return True, "Not Implemented Yet"


# Singleton instance
division_service = DivisionService()
