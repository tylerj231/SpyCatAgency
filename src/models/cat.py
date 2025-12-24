from typing import Optional

from pydantic import BaseModel, Field


class Cat(BaseModel):
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


class CatCreate(Cat):
    pass


class CatUpdate(BaseModel):

    salary: Optional[float] = Field(
        description="The salary of the cat",
        default=None,
    )


class CatDelete(BaseModel):
    id: int = Field(description="The id of the cat to delete")
