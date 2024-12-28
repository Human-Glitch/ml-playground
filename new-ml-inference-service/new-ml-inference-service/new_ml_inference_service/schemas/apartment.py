"""
Schema for apartment
"""

from pydantic import BaseModel


class Apartment(BaseModel):

    """
    area (int): The total area of the apartment in square meters.
    constraction_year (int): The year the apartment was constructed.
    bedrooms (int): The number of bedrooms in the apartment.
    garden_area (int): The area of the garden in square meters, if present.
    balcony_present (int): Indicates if a balcony is present.
    parking_present (int): Indicates if parking is available.
    furnished (int): Indicates if the apartment is furnished.
    garage_present (int): Indicates if a garage is present.
    storage_present (int): Indicates if storage space is available.
    """

    area: int
    constraction_year: int
    bedrooms: int
    garden_area: int
    balcony_present: int
    parking_present: int
    furnished: int
    garage_present: int
    storage_present: int
