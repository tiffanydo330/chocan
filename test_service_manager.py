import pytest
import json
from tempfile import NamedTemporaryFile

# Fixture to create a temporary file
@pytest.fixture
def temp_file():
    with NamedTemporaryFile(mode='w+', delete=False) as tmpfile:
        tmpfile.write(json.dumps([
            {"service_code": "001", "name": "General Consultation", "cost": 1500.99},
            {"service_code": "002", "name": "Dental Cleaning", "cost": 800.99}
        ]))
        tmpfile.seek(0)
        yield tmpfile.name

# Test adding a service
def test_add_service(temp_file):
    manager = ServiceManager(temp_file)
    manager.add_service("003", "X-ray Imaging", 2000.5)
    assert len(manager.services) == 3
    assert manager.services[-1]['name'] == "X-ray Imaging"

# Test removing a service
def test_remove_service(temp_file):
    manager = ServiceManager(temp_file)
    manager.remove_service("001")
    assert len(manager.services) == 1
    assert manager.services[0]['service_code'] != "001"

# Test listing services
def test_list_services(temp_file):
    manager = ServiceManager(temp_file)
    assert len(manager.services) == 2
    assert manager.services[0]['name'] == "General Consultation"
    assert manager.services[1]['name'] == "Dental Cleaning"

# Test saving to file
def test_save_to_file(temp_file):
    manager = ServiceManager(temp_file)
    manager.add_service("004", "Blood Test", 5000.99)
    manager.save_services()

    with open(temp_file, 'r') as file:
        data = json.load(file)
    
    assert len(data) == 3
    assert data[-1]['name'] == "Blood Test"
