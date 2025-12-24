from typing import Optional

from pydantic import BaseModel, Field, field_validator, ConfigDict

from src.models.target import TargetModel, TargetCreate


class MissionModel(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int = Field(
        description="The id of the mission",
    )
    cat_id: int = Field(
        description="The id of the cat assigned to the mission",
        examples=[1],
    )
    targets: list[TargetModel] = Field(
        description="The targets of the cat",
        examples=[
            [
                {
                    "id": 1,
                    "name": "Target #1",
                    "country": "United States.",
                    "notes": "Extreme caution required.",
                    "complete": False,
                }
            ]
        ],
        min_length=1,
        max_length=3,
    )
    complete: bool = Field(
        description="Mission completion status",
        examples=[False],
        default=False,
    )


class MissionCreate(BaseModel):
    cat_id: int = Field(
        description="The id of the cat assigned to the mission",
        examples=[1],
    )
    targets: list[TargetCreate] = Field(
        description="The targets of the cat",
        min_length=1,
        max_length=3,
    )
    complete: bool = Field(
        description="Mission completion status",
        default=False,
    )

    @field_validator("targets", mode="after")
    @classmethod
    def validate_mission_targets(
        cls, targets: list[TargetModel]
    ) -> list[TargetModel] | None:
        if not 1 <= len(targets) <= 3:
            raise ValueError("Mission must have between 1 and 3 targets")
        return targets


class MissionUpdate(BaseModel):
    complete: Optional[bool] = Field(
        description="Mission completion status",
        default=None,
    )
    cat_id: Optional[int] = Field(
        description="Assign cat to the mission. ",
        default=None,
    )


class MissionFilter(BaseModel):
    mission_id: Optional[int] = Field(
        description="The id of the mission",
        default=None,
    )

    cat_id: Optional[int] = Field(
        description="Filter by id of the cat assigned to the mission.",
        default=None,
    )
