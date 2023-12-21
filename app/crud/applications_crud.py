from app.crud.base import CRUDBase
from app.models.applications import Applications
from app.schemas.applications import ApplicationSchema


class CRUDApplication(CRUDBase[Applications, ApplicationSchema]):
    """Applications CRUD class"""
    pass


application = CRUDApplication(Applications)
