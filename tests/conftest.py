"""
Setup sqlite db for tests
"""
from typing import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, StaticPool
from sqlalchemy.orm import sessionmaker
from app.db.base_class import Base
from app.db.get_db import get_db
from app.main import app
from app.models.applications import Applications
from app.models.lines_coverage import LinesCoverage
from app.models.pivot_tables import association_table

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)

Base.metadata.create_all(bind=engine, tables=[
    association_table,
    LinesCoverage.__table__,
    Applications.__table__,
])  # type: ignore[attr-defined]

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        Base.metadata.drop_all(bind=engine)
        db.close()


@pytest.fixture(scope="session")
def db() -> Generator:
    session = TestingSessionLocal()
    yield session
    session.close()


@pytest.fixture(scope="session")
def client() -> Generator:
    """Override test client with local db

    Yields:
        Generator: TestClient
    """
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c
