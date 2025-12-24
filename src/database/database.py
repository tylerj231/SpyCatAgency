from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship

from src.database.config import engine, SessionLocal


class Base(DeclarativeBase):
    pass


class Cat(Base):
    __tablename__ = "cats"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    years_of_experience = Column(Integer, nullable=False)
    breed = Column(String, nullable=False)
    salary = Column(Float, nullable=False)

    mission = relationship(
        "Mission", back_populates="cat", uselist=False, cascade="all, delete-orphan"
    )


class Mission(Base):
    __tablename__ = "missions"

    id = Column(Integer, primary_key=True, index=True)
    cat_id = Column(Integer, ForeignKey("cats.id"), unique=True, nullable=False)
    complete = Column(Boolean, default=False, nullable=False)

    cat = relationship("Cat", back_populates="mission")
    targets = relationship(
        "Target", back_populates="mission", cascade="all, delete-orphan"
    )


class Target(Base):
    __tablename__ = "targets"

    id = Column(Integer, primary_key=True, index=True)
    mission_id = Column(Integer, ForeignKey("missions.id"), nullable=False)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    notes = Column(String, nullable=True)
    complete = Column(Boolean, default=False, nullable=False)

    mission = relationship("Mission", back_populates="targets")


Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
