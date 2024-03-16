import json  # Importing the json module to work with JSON data
from data import Member, Provider  # Importing custom data models
from schema import MemberSchema, ProviderSchema  # Importing schemas for data serialization
from typing import Dict, Any  # Importing type hints for data types
from marshmallow import Schema, fields, post_load
from Carl_Swin import sum_rep_main, EFT_file, print_format, make_dir
from datetime import datetime
from data_management import DataManager
import os
import pathlib
import pytest

MyData = DataManager()
provider_data = MyData.load_data_from_json('providers_pytest.json')
provider_schema = ProviderSchema(many=True)
providers_dict: Dict[str, Member] = {provider.id_num: provider for provider in provider_schema.load(provider_data)}

def test_sum_rep_main():
    assert sum_rep_main(providers_dict) == 0

    fd = open(pathlib.Path(os.getcwd() + "/EFT/EFT_Total"), "r")
    assert fd.read() == "Dr. Smith\a100001\a250.0\nDr. Johnson\a100002\a800.0\nTotal: $1050.0"
    fd.close()

def test_make_dir():
    assert make_dir("<<>>") == 1

def test_EFT_file():
    DestPath = pathlib.Path(str(os.getcwd()) + "/Testing/test-Carl-Swin-Dir")
    assert make_dir( "Testing/test-Carl-Swin-Dir" ) == 0

    assert EFT_file("", None, "", None) == 3 
    
    assert EFT_file(DestPath, None, 123456789, None) == 2 
    assert EFT_file(DestPath, None, "Pytest-file.txt", None) == 2 
    
    for id_num, Prov in providers_dict.items():
        assert EFT_file(DestPath, Prov, "Pytest-file.txt", None) == 1 

    #os.remove( pathlib.Path(str(DestPath) + "/123456789") )
    #os.remove( pathlib.Path(str(DestPath) + "/Pytest-file.txt") )


def test_print_format():
    assert print_format("", None) == 1

    for id_num, Prov in providers_dict.items():
        assert print_format(id_num, Prov) == 0
