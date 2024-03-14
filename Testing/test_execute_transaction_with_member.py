import pytest
import json
import pytest
from unittest.mock import patch

# Assuming your functions are in a file named 'main.py'
from execute_transaction_with_member import validate_member_id, get_provider_info, get_service_details, get_summary_info, add_new_member
'''
Execute transaction with member
	- Validate member ID
	- Take input for transaction report
	- Record/update appropriate transaction data to members.json and providers.json 
	- Refresh the memory with the new file data
'''

def test_validate_member_id():
    member_data = [
        {"name": "John Doe", "id_num": "000001"},
        {"name": "Jane Smith", "id_num": "000002"}
    ]
    is_valid, message = validate_member_id(member_data)
    assert is_valid == True
    assert message == "All member IDs are VALID"

@patch('builtins.input', side_effect=["Dr. Smith", "12345", "123 Main St, Anytown, NY, 12345"])
def test_get_provider_info(input):
    provider_name, provider_number, provider_address = get_provider_info()
    assert provider_name == "Dr. Smith"
    assert provider_number == "12345"
    assert provider_address == "123 Main St, Anytown, NY, 12345"

# Add similar tests for get_service_details and get_summary_info

@patch('builtins.input', side_effect=["John Doe", "000003", "123 Main St", "Anytown", "NY", "12345"])
def test_add_new_member(input):
    new_member = add_new_member()
    assert new_member["name"] == "John Doe"
    assert new_member["id_num"] == "000003"
    assert new_member["street"] == "123 Main St"
    assert new_member["city"] == "Anytown"
    assert new_member["state"] == "NY"
    assert new_member["zip_code"] == "12345"
    assert new_member["services"] == []