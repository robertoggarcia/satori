from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from tests.factories.applications import ApplicationsFactory
from app.crud.applications_crud import application as application_crud


def test_get_applications(client: TestClient, db: Session) -> None:
    """Test API GET /api/v1/applications endpoint"""
    obj = ApplicationsFactory.stub().__dict__
    application_crud.create(db=db, obj_in=obj)

    response = client.get("/api/v1/applications")
    assert response.status_code == 200
    data = response.json()
    assert "items" in data
    assert len(data["items"]) > 0
    assert "application_id" in data["items"][0]
    assert "account_name" in data["items"][0]
    assert "lines_coverage" in data["items"][0]
    assert "uw_name" in data["items"][0]
    assert "premium" in data["items"][0]
    assert "state" in data["items"][0]
    assert "effective_date" in data["items"][0]
    assert "expiration_date" in data["items"][0]
    assert "sic" in data["items"][0]
    assert "status" in data["items"][0]
    assert "deal_stage" in data["items"][0]
    assert "lines_coverage" in data["items"][0]
