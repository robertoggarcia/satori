from typing import List, Dict

from fastapi.encoders import jsonable_encoder
from fastapi import Query, APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud.applications_crud import application
from app.db.get_db import get_db
from app.schemas.applications import ApplicationSchema

router = APIRouter()


@router.get("", summary="List applications", response_model=Dict[str, List[ApplicationSchema]])
async def get_applications(
    db: Session = Depends(get_db),
    skip: int = Query(0, description="Número de elementos a omitir"),
    limit: int = Query(10, description="Número máximo de elementos a devolver"),
):
    paginated_applications = application.filter(db=db, skip=skip, limit=limit)
    data = [
        ApplicationSchema(**{
            **jsonable_encoder(_application),
            "lines_coverage": [line.name for line in _application.lines_coverage],
        })
        for _application in paginated_applications
    ]
    return {"items": data}
