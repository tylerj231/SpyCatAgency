from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class TargetModel(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: Optional[int] = Field(
        description="The id of the target",
        default=None,
    )
    mission_id: int = Field(description="The mission this target belongs to")

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


class TargetCreate(BaseModel):
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


class TargetUpdate(BaseModel):
    notes: Optional[str] = Field(default=None)
    complete: Optional[bool] = Field(default=None)
