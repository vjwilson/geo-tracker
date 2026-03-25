"""Text utility functions"""


def decode_country_name(country_name: str) -> str:
    """Decode URL-encoded country name to proper format

    Args:
        country_name: URL-encoded country name with hyphens instead of spaces

    Returns:
        Properly formatted country name with title case
    """
    # Replace hyphens with spaces and title case
    decoded = country_name.replace("-", " ").title()

    # Fix small words that should be lowercase (and, the, of)
    decoded = decoded.replace(" And ", " and ")
    decoded = decoded.replace(" The ", " the ")
    decoded = decoded.replace(" Of ", " of ")

    return decoded
