import pytest
import os
# import provider report file with the associated methods
from providerReport import generate_provider_report, format_field
# import relevant classes from data file (Provider and ProviderService)
from data import Provider, ProviderService 

def test_successful_report_generation():
    # init provider with name, id, street, city, state, services, num consultations, total week fee
    provider = Provider("Jane Doe", "123456789", "123 Street St", "Portland", "OR", "12345", [], 0, 0.0)
    services = [ProviderService("01-02-2023", "01-02-2023 12:34:44", "John Doe", "123456789", "123456", 100.00)]
    file_name = generate_provider_report(provider, services)
    assert os.path.exists(file_name)
    os.remove(file_name)  # remove

def test_invalid_data_handling():
    # setting parameters to satisfy init for provider and services
    provider = Provider(None, "123456789", None, "Portland", "OR", "12345", [], 0, 0.0)
    services = [ProviderService("01-01-2023", None, "John Doe", "123456789", "123456", 100.00)]
    file_name = generate_provider_report(provider, services)
    assert file_name is None  # Expecting None due to invalid data

def test_file_naming():
    # setting parameters again to satisfy init for provider and services
    provider = Provider("Jane Doe", "123456789", "123 Street St", "Portland", "OR", "12345", [], 0, 0.0)
    services = [ProviderService("01-01-2023", "01-02-2023 12:34:44", "Member One", "123456789", "123456", 100.00)]
    file_name = generate_provider_report(provider, services)
    expected_file_name = "Jane_Doe.json"
    assert file_name == expected_file_name  # checking filename
    os.remove(file_name)  # remove

def test_empty_provider_details():
    provider = Provider("", "", "", "", "", "", [], 0, 0.0)
    services = []
    file_name = generate_provider_report(provider, services)
    assert file_name is None 

def test_special_characters_in_provider_name():
    provider = Provider("Provi@#er$%^", "123456789", "123 Main St", "City", "ST", "12345", [], 0, 0.0)
    services = []
    file_name = generate_provider_report(provider, services)
    assert file_name is None # should not work due to isalpha check

def test_provider_with_all_numeric_fields():
    provider = Provider("123456", "123456789", "123456789", "1234567", "12", "12345", [], 0, 0.0)
    services = [ProviderService("01-01-2023", "01-02-2023 12:34:44", "123456", "123456789", "123456", 100.00)]
    file_name = generate_provider_report(provider, services)
    assert file_name is None # all numnbers should not work either

def test_with_multiple_services():
    provider = Provider("Multi Service Provider", "123456789", "123 Multi St", "MultiCity", "MC", "12345", [], 0, 0.0)
    services = [
        ProviderService("01-01-2023", "01-02-2023 12:34:44", "Multi One", "987654321", "654321", 200.00),
        ProviderService("02-01-2023", "02-02-2023 13:34:44", "Multi Two", "987650123", "654320", 300.00)
    ]
    file_name = generate_provider_report(provider, services)
    assert os.path.exists(file_name)
    os.remove(file_name)

def test_report_without_services():
    provider = Provider("No Service Provider", "123456789", "No Service St", "NoCity", "NC", "12345", [], 0, 0.0)
    services = []
    file_name = generate_provider_report(provider, services)
    assert os.path.exists(file_name)
    os.remove(file_name)

def test_report_with_max_field_lengths():
    provider = Provider("A" * 25, "123456789", "A" * 25, "A" * 14, "AA", "12345", [], 0, 0.0)
    services = [ProviderService("01-01-2023", "01-01-2023 10:00:00", "A" * 25, "123456789", "123456", 999.99)]
    file_name = generate_provider_report(provider, services)
    assert os.path.exists(file_name)
    os.remove(file_name)

def test_non_english_characters_in_provider_name():
    # just in case! 
    provider = Provider("Provïdêr Ñámé", "123456789", "123 Main St", "City", "ST", "12345", [], 0, 0.0)
    services = [ProviderService("01-01-2023", "01-02-2023 12:34:44", "John Doe", "123456789", "123456", 100.00)]
    file_name = generate_provider_report(provider, services)
    assert os.path.exists(file_name)
    os.remove(file_name)