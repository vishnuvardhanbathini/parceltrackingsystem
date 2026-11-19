
import pytest
import sqlite3
import database
import courier
from courier import Courier

@pytest.fixture
def setup_db(tmp_path, monkeypatch):
    db_path = tmp_path / "test.db"

    def test_connect():
        return sqlite3.connect(str(db_path))

    monkeypatch.setattr(database, "connect", test_connect)
    monkeypatch.setattr(courier, "connect", test_connect)

    database.create_tables()

    return Courier()

def test_add_customer(setup_db):
    assert setup_db.add_customer(
        "Ravi", "9876543210", "Warangal"
    ) == 1

def test_register_parcel(setup_db):
    c = setup_db
    cid = c.add_customer("Ravi", "9876543210", "Warangal")
    assert c.register_parcel(cid, "Hyderabad") == 1

def test_track_parcel(setup_db):
    c = setup_db
    cid = c.add_customer("Ravi", "9876543210", "Warangal")
    pid = c.register_parcel(cid, "Hyderabad")
    assert c.track_parcel(pid)[3] == "Booked"

def test_update_status(setup_db):
    c = setup_db
    cid = c.add_customer("Ravi", "9876543210", "Warangal")
    pid = c.register_parcel(cid, "Hyderabad")
    assert c.update_status(pid, "Delivered") is True

def test_invalid_parcel(setup_db):
    assert setup_db.update_status(999, "Delivered") is False

def test_view_customers(setup_db):
    c = setup_db
    c.add_customer("Ravi", "9876543210", "Warangal")
    assert len(c.view_customers()) == 1
