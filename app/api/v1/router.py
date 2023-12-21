from fastapi import APIRouter, status

from app.api.v1.endpoints import applications

api_router = APIRouter()

api_router.include_router(
    applications.router,
    prefix="/applications",
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)
