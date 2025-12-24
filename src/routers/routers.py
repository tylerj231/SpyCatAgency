from fastapi import APIRouter

from src.routers.cats.cat import cats_router
from src.routers.missions.mission import mission_router
from src.routers.targets.target import target_router

base_router = APIRouter(
    prefix="/api/vi/spy-cat-agency",
)
base_router.include_router(cats_router)
base_router.include_router(mission_router)
base_router.include_router(target_router)
