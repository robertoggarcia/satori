from sqlalchemy import Column, ForeignKey
from sqlalchemy.testing.schema import Table

from app.db.base_class import Base

association_table = Table(
    "application_lines_coverage",
    Base.metadata,
    Column("application_id", ForeignKey("applications.application_id"), primary_key=True),
    Column("lines_coverage_id", ForeignKey("lines_coverage.lines_coverage_id"), primary_key=True),
)
