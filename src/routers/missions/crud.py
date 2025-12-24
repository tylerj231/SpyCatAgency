from fastapi import Depends
from pydantic import ValidationError
from sqlalchemy.orm import Session


from src.models.mission import MissionModel, MissionFilter, MissionUpdate, MissionCreate
from src.database.database import get_db, object_to_dict, Mission, Target
from src.exceptions.mission_not_found_exception import MissionNotFoundException
from src.exceptions.mission_complete_exception import (
    MissionCompleteException,
)


def create_mission(
    mission: MissionCreate, db: Session = Depends(get_db)
) -> MissionModel:
    """
    Create a mission in the database.
    :param mission:
    :param db:
    :return:
    """
    mission_dict = mission.model_dump()
    targets = mission_dict.pop("targets", [])

    mission_record = Mission(**mission_dict)
    db.add(mission_record)
    db.flush()

    for target in targets:
        target.pop("id", None)
        target = Target(mission_id=mission_record.id, **target)
        db.add(target)

    db.commit()
    db.refresh(mission_record)

    return MissionModel.model_validate(mission_record)


def retrieve_missions(db: Session = Depends(get_db)) -> list[MissionModel]:
    """
    Get all missions from the database.
    :param db:
    :return:
    """
    missions = db.query(Mission).all()
    missions = [object_to_dict(mission) for mission in missions]
    return [MissionModel.model_validate(mission) for mission in missions]


def retrieve_mission(
    filters: MissionFilter, db: Session = Depends(get_db)
) -> MissionModel | None:
    """
    Get a specific mission from the database.
    :param filters:
    :param db:
    :return:
    """
    cat_id = filters.cat_id
    mission_id = filters.mission_id

    mission = None

    if cat_id:
        mission = db.query().filter(Mission.cat_id == cat_id).first()

    if mission_id:
        mission = db.query(Mission).filter(Mission.id == mission_id).first()

    try:
        return MissionModel.model_validate(object_to_dict(mission))

    except ValidationError:
        raise MissionNotFoundException


def update_mission(
    mission_id: int, mission_update: MissionUpdate, db: Session = Depends(get_db)
) -> None:
    """
    Update a specific mission in the database.
    :param mission_id:
    :param mission_update:
    :param db:
    :return:
    """
    mission = db.query(Mission).filter(Mission.id == mission_id).first()

    if not mission:
        raise MissionNotFoundException

    if mission.complete:
        raise MissionCompleteException

    if mission_update.complete:
        mission.complete = mission_update.complete

    if mission_update.cat_id:
        mission.cat_id = mission_update.cat_id

    db.add(mission)
    db.commit()
    db.refresh(mission)


def remove_mission(mission_id: int, db: Session = Depends(get_db)) -> None:
    """
    Remove a specific mission from the database.
    :param mission_id:
    :param db:
    :return:
    """
    mission = db.query(Mission).filter(Mission.id == mission_id).first()

    if not mission:
        raise MissionNotFoundException

    db.delete(mission)
    db.commit()
