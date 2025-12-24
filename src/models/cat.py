from typing import Optional

import httpx
from pydantic import BaseModel, Field, field_validator, ConfigDict

from src.exceptions.invalid_cat_breed_exception import InvalidCatBreedException


class CatModel(BaseModel):
    """
    Pydantic Schema for Spy Cat.
    """

    model_config = ConfigDict(from_attributes=True)

    id: Optional[int] = Field(
        description="The id of the cat",
        default=None,
    )
    name: str = Field(
        description="The name of the cat",
        examples=["mr.Paws"],
    )
    experience: int = Field(
        description="Years of experience",
        examples=[1],
    )
    breed: str = Field(
        description="The breed of the cat",
        examples=["Persian"],
    )
    salary: float = Field(
        description="The salary of the cat",
        examples=[1500.0],
        ge=0,
    )


class CatCreate(BaseModel):
    """
    Pydantic Schema to create a Spy Cat.
    Raises: InvalidCatBreedException if cat breed is not valid.
    """

    name: str = Field(
        description="The name of the cat",
        examples=["mr.Paws"],
    )
    experience: int = Field(
        description="Years of experience",
        examples=[1],
    )
    breed: str = Field(
        description="The breed of the cat",
        examples=["Persian"],
    )
    salary: float = Field(
        description="The salary of the cat",
        examples=[1500.0],
        ge=0,
    )

    @staticmethod
    def get_cat_breeds():
        with httpx.Client() as client:
            response = client.get("https://api.thecatapi.com/v1/breeds")
            response.raise_for_status()
            data = response.json()
            return [cat.get("name") for cat in data]

    @field_validator("breed", mode="after")
    @classmethod
    def validate_breed(cls, breed: str) -> str | None:
        breeds = cls.get_cat_breeds()
        if breed not in breeds:
            raise InvalidCatBreedException(breed)
        return breed


class CatUpdate(BaseModel):
    """
    Pydantic Schema to update a Spy Cat's salary.
    """

    salary: Optional[float] = Field(
        description="The salary of the cat",
        default=None,
    )


class CatDelete(BaseModel):
    """
    Pydantic Schema to delete a Spy Cat.
    """

    id: int = Field(description="The id of the cat to delete")
