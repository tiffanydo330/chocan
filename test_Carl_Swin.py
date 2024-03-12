from schema import MemberSchema, ProviderSchema
from main import load_data_from_json
from data import Member, Provider
from typing import Dict, Any
from Carl_Swin import sum_rep_main, EFT_file, print_format, make_dir
import os
import pathlib
import pytest

provider_data = load_data_from_json('providers_pytest.json')
provider_schema = ProviderSchema(many=True) 
providers_dict: Dict[str, Member] = {provider.id_num: provider for provider in provider_schema.load(provider_data)}

def test_sum_rep_main():
    assert sum_rep_main(providers_dict) == 0

    fd = open(pathlib.Path(os.getcwd() + "/EFT/EFT_Total"), "r")
    assert fd.read() == "Dr. Smith\a100001\a250.0\nDr. Johnson\a100002\a800.0\nTotal: $1050.0"
    fd.close()

def test_EFT_file():
    assert EFT_file("", None, "", None) == 3 

    assert EFT_file("", None, 123456789, None) == 2 
    assert EFT_file("", None, "Pytest_file.txt", None) == 2 

    for id_num, Prov in providers_dict.items():
        assert EFT_file("", Prov, "Pytest_file.txt", None) == 1 

def test_print_format():
    assert print_format("", None) == 1

    for id_num, Prov in providers_dict.items():
        assert print_format(id_num, Prov) == 0

def test_make_dir():
    assert make_dir("<<>>") == 1