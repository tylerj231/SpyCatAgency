from typing import Optional

from pydantic import BaseModel, Field


class Target(BaseModel):
    name: str = Field(
        description="The name of the target",
    )
    country: str = Field(
        description="The country of the target",
    )
    notes: Optional[str] = Field(
        description="The notes of the target",
        default=None,
    )
    complete: bool = Field(
        description="Target completion status",
    )


class TargetCreate(Target):
    pass


class TargetUpdate(BaseModel):
    name: Optional[str] = Field(default=None)
    country: Optional[str] = Field(default=None)
    notes: Optional[str] = Field(default=None)
    complete: Optional[bool] = Field(default=None)
