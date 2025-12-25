from fastapi import HTTPException, Depends, status
from sqlalchemy.orm import Session

from src.database.database import Cat
from src.database.database import get_db
from src.models.cat import CatModel, CatCreate, CatUpdate
from src.exceptions.spy_cat_not_found_exception import SpyCatNotFoundException


def create_spy_cat(cat: CatCreate, db: Session = Depends(get_db)) -> CatModel:
    """
    Create a new spy cat in the database.
    :param cat:
    :param db:
    :return:
    """

    cat_dict = cat.model_dump()
    cat_record = Cat(**cat_dict)
    db.add(cat_record)
    db.commit()
    db.refresh(cat_record)

    return CatModel.model_validate(cat_record)


def query_cats(db: Session = Depends(get_db)) -> list[CatModel] | None:
    """
    Query all cats in the database.
    :param db:
    :return:
    """
    cats = db.query(Cat).all()
    if not cats:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"message": "No spy cats were found at this time."},
        )
    return [CatModel.model_validate(cat) for cat in cats]


def query_cat(cat_id: int, db: Session = Depends(get_db)) -> CatModel | None:
    """
    Query a specific spy cat.
    :param cat_id:
    :param db:
    :return:
    """
    cat = db.query(Cat).filter(Cat.id == cat_id).first()
    if not cat:
        raise SpyCatNotFoundException(cat_id)

    return CatModel.model_validate(cat)


def update_cat_salary(
    cat_id: int, cat_salary: CatUpdate, db: Session = Depends(get_db)
) -> None:
    """
    Update a spy cat's salary.
    :param cat_id:
    :param cat_salary:
    :param db:
    :return:
    """
    cat = db.query(Cat).filter(Cat.id == cat_id).first()
    if not cat:
        raise SpyCatNotFoundException(cat_id)
    cat.salary = cat_salary.salary
    db.add(cat)
    db.commit()
    db.refresh(cat)
