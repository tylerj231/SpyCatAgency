from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.database.database import get_db
from src.models.target import TargetUpdate
from src.routers.targets.crud import update_target

target_router = APIRouter(
    tags=["Target"],
)


@target_router.patch("/targets/{target_id}", status_code=status.HTTP_204_NO_CONTENT)
def patch_target(
    target_id: int, target: TargetUpdate, db: Session = Depends(get_db)
) -> None:
    update_target(target_id, target, db)
