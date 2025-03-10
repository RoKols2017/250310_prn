from app.db import crud, schemas
from app.models import building, department, user

def test_create_building(db_session):
    new_building = schemas.BuildingCreate(code="A1", name="Main Office")
    created = crud.create_building(db_session, new_building)
    assert created.code == "A1"
    assert created.name == "Main Office"

def test_get_building(db_session):
    new_building = schemas.BuildingCreate(code="B2", name="Secondary Office")
    crud.create_building(db_session, new_building)
    found = crud.get_building(db_session, "B2")
    assert found is not None
    assert found.name == "Secondary Office"
