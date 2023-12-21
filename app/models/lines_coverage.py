import datetime

from sqlalchemy import Column, String, Integer, DateTime, Boolean

from app.db.base_class import Base


class LinesCoverage(Base):
    __tablename__ = "lines_coverage"

    lines_coverage_id = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    active = Column(Boolean, default=True)
