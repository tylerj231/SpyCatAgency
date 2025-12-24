from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status

from src.database.database import Cat, object_to_dict
from src.database.database import get_db
from src.models.cat import CatModel, CatCreate, CatUpdate
from src.exceptions.spy_cat_not_found_exception import SpyCatNotFoundException


def create_spy_cat(cat: CatCreate, db: Session = Depends(get_db)) -> CatModel:
    cat_dict = cat.model_dump()
    cat_record = Cat(**cat_dict)
    db.add(cat_record)
    db.commit()
    db.add(cat_record)
    db.commit()
    db.refresh(cat_record)

    return CatModel.model_validate(cat_dict)


def query_cats(db: Session = Depends(get_db)) -> list[CatModel] | None:
    cats = db.query(Cat).all()
    if not cats:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"message": "No spy cats were found at this time."},
        )
    return [CatModel.model_validate(cat) for cat in cats]


def query_cat(cat_id: int, db: Session = Depends(get_db)) -> CatModel | None:
    cat = db.query(Cat).filter(Cat.id == cat_id).first()
    if not cat:
        raise SpyCatNotFoundException(cat_id)

    cat = object_to_dict(cat)
    return CatModel.model_validate(cat)


def update_cat_salary(
    cat_id: int, cat_salary: CatUpdate, db: Session = Depends(get_db)
) -> None:
    cat = db.query(Cat).filter(Cat.id == cat_id).first()
    if not cat:
        raise SpyCatNotFoundException(cat_id)
    cat.salary = cat_salary.salary
    db.add(cat)
    db.commit()
    db.refresh(cat)
