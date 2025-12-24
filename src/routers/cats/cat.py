from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from src.database.database import get_db
from src.models.cat import CatModel, CatCreate, CatUpdate
from src.routers.cats.crud import (
    query_cats,
    create_spy_cat,
    query_cat,
    update_cat_salary,
)

cats_router = APIRouter(tags=["Cats"])


@cats_router.post(
    "/spy-cats", response_model=CatModel, status_code=status.HTTP_201_CREATED
)
def post_spy_cat(cat: CatCreate, db: Session = Depends(get_db)) -> CatModel:
    """
    Endpoint to create a spy cat.
    :param cat:
    :param db:
    :return:
    """
    return create_spy_cat(cat, db)


@cats_router.get(
    "/spy-cats", response_model=list[CatModel] | None, status_code=status.HTTP_200_OK
)
def get_cats(db: Session = Depends(get_db)) -> list[CatModel] | None:
    """
    Endpoint to retrieve all spy cats.
    :param db:
    :return:
    """
    return query_cats(db)


@cats_router.get(
    "/spy-cats/{cat_id}", response_model=CatModel, status_code=status.HTTP_200_OK
)
def get_cat(cat_id: int, db: Session = Depends(get_db)) -> CatModel:
    """
    Endpoint to retrieve a specific spy cat.
    :param cat_id:
    :param db:
    :return:
    """
    return query_cat(cat_id, db)


@cats_router.patch("/spy-cats/{cat_id}", status_code=status.HTTP_204_NO_CONTENT)
def patch_cat(
    cat_id: int, cat_salary: CatUpdate, db: Session = Depends(get_db)
) -> None:
    """
    Endpoint to update a spy cat's salary.
    :param cat_id:
    :param cat_salary:
    :param db:
    :return:
    """
    update_cat_salary(cat_id, cat_salary, db)
