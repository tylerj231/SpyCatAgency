from pydantic import BaseModel, Field, field_validator

from database.database import Target


class Mission(BaseModel):
    id: int = Field(description="The id of the mission")
    cat_id: int = Field(description="The id of the cat assigned to the mission")
    targets: list[Target] = Field(
        description="The targets of the cat",
        min_length=1,
        max_length=3,
    )
    complete: bool = Field(
        description="Mission completion status",
        default=False,
    )


class MissionCreate(Mission):

    @field_validator("targets", mode="after")
    @classmethod
    def validate_mission_targets(cls, targets: list[Target]) -> list[Target] | None:
        if not 1 <= len(targets) <= 3:
            raise ValueError("Mission must have between 1 and 3 targets")
        return targets


class MissionUpdate(BaseModel):
    targets: list[Target] = Field(
        description="The targets of mission.",
    )
