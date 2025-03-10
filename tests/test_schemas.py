from app.db.schemas import BuildingCreate

def test_building_schema():
    building = BuildingCreate(code="HQ1", name="Headquarters")
    assert building.code == "HQ1"
    assert building.name == "Headquarters"
