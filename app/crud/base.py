from typing import Generic, List, Type, TypeVar

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)
SchemaType = TypeVar("SchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, SchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        Args:

        `model`: A SQLAlchemy model class
        `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def filter(self, db: Session, skip: int = 0, limit: int = 10, **kwargs) -> List[ModelType]:
        """Get a list of ModelType filtered by **kwargs"""
        return db.query(self.model).filter_by(**kwargs).offset(skip).limit(limit).all()

    def create(self, db: Session, *, obj_in: SchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in) if type(obj_in) is not dict else obj_in
        db_obj = self.model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
