import factory
from app.models.applications import Applications
from datetime import date
from tests.conftest import TestingSessionLocal


class ApplicationsFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Applications
        sqlalchemy_session = TestingSessionLocal

    application_id = factory.Sequence(lambda n: n)
    account_name = factory.Faker("company")
    uw_name = factory.Faker("name")
    premium = 12000
    state = "DC"
    effective_date = factory.LazyFunction(date.today)
    expiration_date = factory.LazyFunction(date.today)
    sic = "01011 Iron Ores"
    status = "new"
    deal_stage = "new"
    created_at = factory.Faker("date_time")
    active = True
