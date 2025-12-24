from fastapi import Depends
from sqlalchemy.orm import Session

from database.database import get_db, Target, Mission
from exceptions.mission_complete_exception import (
    MissionCompleteException,
    MissionCompleteExceptionTarget,
)
from exceptions.target_not_found_exception import TargetNotFoundException
from models.target import TargetUpdate


def update_target(
    target_id: int,
    target: TargetUpdate,
    db: Session = Depends(get_db),
) -> None:
    target_record = db.query(Target).filter(Target.id == target_id).first()

    if not target_record:
        raise TargetNotFoundException

    mission = db.query(Mission).filter(Mission.id == target_record.mission_id).first()

    if target_record.notes:

        if mission.complete:
            raise MissionCompleteException

        if target_record.complete:
            raise MissionCompleteExceptionTarget

        target_record.notes = target.notes

    if target.complete:
        target_record.complete = target.complete

    db.commit()
    db.refresh(target_record)
