"""Pydantic models for API request/response validation"""

from pydantic import BaseModel


class CountryResponse(BaseModel):
    """Response model for a single country"""
    name: str


class CountryListResponse(BaseModel):
    """Response model for a list of countries"""
    countries: list[str]


class DivisionListResponse(BaseModel):
    """Response model for administrative divisions"""
    country: str
    divisions: list[str]


class ErrorResponse(BaseModel):
    """Response model for errors"""
    detail: str
