import datetime

from sqlalchemy import Column, String, Float, Integer, Date, DateTime, Boolean
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.lines_coverage import LinesCoverage
from app.models.pivot_tables import association_table


class Applications(Base):
    __tablename__ = "applications"

    application_id = Column(Integer, primary_key=True)
    account_name = Column(String)
    uw_name = Column(String)
    premium = Column(Float)
    state = Column(String)
    effective_date = Column(Date)
    expiration_date = Column(Date)
    sic = Column(String)
    status = Column(String)
    deal_stage = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    active = Column(Boolean, default=True)
    lines_coverage = relationship("LinesCoverage", secondary="application_lines_coverage", back_populates='applications')
