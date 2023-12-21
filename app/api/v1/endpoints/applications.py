from typing import List

from fastapi import Query, APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud.applications_crud import application
from app.db.get_db import get_db
from app.schemas.applications import ApplicationSchema

router = APIRouter()


@router.get("", summary="List applications")
async def get_applications(
    db: Session = Depends(get_db),
    skip: int = Query(0, description="Número de elementos a omitir"),
    limit: int = Query(10, description="Número máximo de elementos a devolver"),
):
    paginated_applications = application.filter(db=db, skip=skip, limit=limit)
    return {"items": paginated_applications}
