from typing import Annotated

from fastapi import APIRouter, status, Depends, Query
from sqlalchemy.orm import Session

from src.database.database import get_db
from src.routers.missions.crud import (
    retrieve_missions,
    retrieve_mission,
    create_mission,
    remove_mission,
    update_mission,
)
from src.models.mission import MissionModel, MissionFilter, MissionCreate, MissionUpdate

mission_router = APIRouter(tags=["Mission"])


@mission_router.post(
    "/missions", response_model=MissionModel, status_code=status.HTTP_201_CREATED
)
def post_mission(mission: MissionCreate, db: Session = Depends(get_db)) -> MissionModel:
    """
    Endpoint for creating a mission.
    :param mission:
    :param db:
    :return:
    """
    return create_mission(mission, db)


@mission_router.get(
    "/missions", response_model=list[MissionModel], status_code=status.HTTP_200_OK
)
def get_missions(db: Session = Depends(get_db)) -> list[MissionModel]:
    """
    Endpoint for retrieving all missions.
    :param db:
    :return:
    """
    return retrieve_missions(db)


@mission_router.get("/missions/mission", response_model=MissionModel)
def get_mission(
    filters: Annotated[MissionFilter, Query()], db: Session = Depends(get_db)
) -> MissionModel:
    """
    Endpoint for retrieving a specific mission.
    :param filters:
    :param db:
    :return:
    """
    return retrieve_mission(filters, db)


@mission_router.patch("/missions/{mission_id}", status_code=status.HTTP_204_NO_CONTENT)
def patch_mission(
    mission_id: int, mission: MissionUpdate, db: Session = Depends(get_db)
) -> None:
    """
    Endpoint for updating a mission.
    :param mission_id:
    :param mission:
    :param db:
    :return:
    """
    update_mission(mission_id, mission, db)


@mission_router.delete("/missions/{mission_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_mission(mission_id: int, db: Session = Depends(get_db)) -> None:
    """
    Endpoint for deleting a mission.
    :param mission_id:
    :param db:
    :return:
    """
    remove_mission(mission_id, db)
