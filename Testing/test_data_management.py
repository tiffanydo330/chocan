#test_data_management.py

import pytest
#from data_management import DataManager, Member, Provider
#from .. import data_management
from data_management import DataManager, Member, Provider

@pytest.fixture
def data_manager():
    return DataManager()

def test_get_member(data_manager):
    # Test getting a member that exists
    member_id = "123456"
    member_data = Member(name="Test Member", id_num=member_id, street="123 Test St",
                         city="Test City", state="Test State", zip_code="12345", services=[])

    data_manager.add_member(member_id, member_data)

    result = data_manager.get_member(member_id)
    assert result == member_data

    # Test getting a member that does not exist
    result = data_manager.get_member("nonexistent_id")
    assert result is None

def test_remove_member(data_manager):
    # Test removing a member that exists
    member_id = "123456"
    member_data = Member(name="Test Member", id_num=member_id, street="123 Test St",
                         city="Test City", state="Test State", zip_code="12345", services=[])

    data_manager.add_member(member_id, member_data)

    result = data_manager.remove_member(member_id)
    assert result == 0
    assert member_id not in data_manager.get_member_dict()

    # Test removing a member that does not exist
    result = data_manager.remove_member("nonexistent_id")
    assert result == 1

def test_modify_member(data_manager):
    # Test modifying a member that exists
    member_id = "123456"
    member_data = Member(name="Test Member", id_num=member_id, street="123 Test St",
                         city="Test City", state="Test State", zip_code="12345", services=[])

    data_manager.add_member(member_id, member_data)

    new_member_data = Member(name="Updated Member", id_num=member_id, street="456 Updated St",
                             city="Updated City", state="Updated State", zip_code="67890", services=[])

    result = data_manager.modify_member(member_id, new_member_data)
    assert result == 0

    updated_member = data_manager.get_member(member_id)
    assert updated_member == new_member_data

    # Test modifying a member that does not exist
    result = data_manager.modify_member("nonexistent_id", new_member_data)
    assert result == 1

# Add more test cases for other methods...

def test_add_member(data_manager):
    # Test adding a new member
    member_id = "123456"
    member_data = Member(name="Test Member", id_num=member_id, street="123 Test St",
                         city="Test City", state="Test State", zip_code="12345", services=[])

    data_manager.add_member(member_id, member_data)

    result = data_manager.get_member(member_id)
    assert result == member_data

def test_add_provider(data_manager):
    # Test adding a new provider
    provider_id = "654321"
    provider_data = Provider(name="Test Provider", id_num=provider_id, street="456 Test St",
                             city="Test City", state="Test State", zip_code="54321",
                             services=[], num_consultations=0, total_wk_fee=0)

    data_manager.add_provider(provider_id, provider_data)

    result = data_manager.get_provider(provider_id)
    assert result == provider_data

def test_remove_member(data_manager):
    # Test removing a member
    member_id = "123456"
    data_manager.remove_member(member_id)

    result = data_manager.get_member(member_id)
    assert result is None

def test_remove_provider(data_manager):
    # Test removing a provider
    provider_id = "654321"
    data_manager.remove_provider(provider_id)

    result = data_manager.get_provider(provider_id)
    assert result is None

def test_modify_member(data_manager):
    # Test modifying a member
    pre_updated_member = Member(name="Pre Updated Member", id_num="123456", 
            street="123 Test St", city="Test City", state="Test State", 
            zip_code="12345", services=[])

    data_manager.add_member(pre_updated_member.id_num, pre_updated_member)
    
    updated_member_data = Member(name="Updated Member", id_num="654321", 
            street="456 Updated St", city="Updated City", state="Updated State", 
            zip_code="67890", services=[])

    data_manager.modify_member(pre_updated_member.id_num, updated_member_data)

    result = data_manager.get_member(updated_member_data.id_num)
    assert result == updated_member_data

def test_modify_provider(data_manager):
    # Test modifying a provider
    pre_updated_provider = Provider(name="Pre Updated Provider", id_num="123456", 
            street="123 Test St", city="Test City", state="Test State", 
            zip_code="12345", services=[], num_consultations=0, total_wk_fee=0)

    data_manager.add_provider(pre_updated_provider.id_num, pre_updated_provider)

    updated_provider_data = Provider(name="Updated Provider", id_num="654321", 
            street="456 Updated St", city="Updated City", state="Updated State", 
            zip_code="67890", services=[], num_consultations=10, total_wk_fee=100)

    data_manager.modify_provider(pre_updated_provider.id_num, updated_provider_data)

    result = data_manager.get_provider(updated_provider_data.id_num)
    assert result == updated_provider_data

def test_load_data_from_json(data_manager):
    # Test loading data from JSON files
    data_manager.load_data_from_json('members.json')
    data_manager.load_data_from_json('providers.json')

    assert len(data_manager.get_member_dict()) > 0
    assert len(data_manager.get_provider_dict()) > 0

#TODO
def test_write_to_json(data_manager):
    # Test writing data to JSON files
    data_manager.write_all_to_json()

if __name__ == "__main__":
    pytest.main()

