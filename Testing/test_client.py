import pytest
import client

def test_bool_input(monkeypatch, capsys, _client_fixture):
    input_mocks = iter(["", "byes", "bno", "y", "Y", "yes", "Yes", "true", "True", "n", "N", "no", "No", "false", "False"]) 
    monkeypatch.setattr('builtins.input', lambda: next(input_mocks))
    entry = _client_fixture._Client__bool_input()
    all_outputs = (capsys.readouterr()).err.split("\n")
    assert "Error: invalid boolean input ''" in all_outputs
    assert "Error: invalid boolean input 'byes'" in all_outputs
    assert "Error: invalid boolean input 'bno'" in all_outputs
    assert entry == True
    for i in range(5):
        entry = _client_fixture._Client__bool_input()
        assert entry == True
    for i in range(6):
        entry = _client_fixture._Client__bool_input()
        assert entry == False


def test_string_input(monkeypatch, capsys, _client_fixture):
    input_mocks = iter(["", "blablablabablalbad", "Don Hector"]) 
    monkeypatch.setattr('builtins.input', lambda: next(input_mocks))
    string = _client_fixture._Client__string_input(10)
    all_outputs = (capsys.readouterr()).err.split("\n")
    assert "Error: Input must include at least one character" in all_outputs
    assert "Error: Input 10 characters max, but 18 characters given" in all_outputs
    assert string == "Don Hector"


def test_int_input(monkeypatch, capsys, _client_fixture):
    input_mocks = iter(["", "Characters", "99999999999", "3259713"])
    monkeypatch.setattr('builtins.input', lambda: next(input_mocks))
    number = _client_fixture._Client__int_input(10)
    all_outputs = (capsys.readouterr()).err.split("\n")
    assert "Error: Input must include at least one character" in all_outputs
    assert "Error: invalid literal for int() with base 10: 'Characters'" in all_outputs
    assert "Error: Input 10 characters max, but 11 characters given" in all_outputs
    assert number == 3259713


def test_time_input(monkeypatch, capsys, _client_fixture):
    input_mocks = iter(["", "Characters", " 06-20-2000", "06-20-2000 ", "06-20-2000"])
    monkeypatch.setattr('builtins.input', lambda: next(input_mocks))
    time_string = _client_fixture._Client__time_input()
    all_outputs = (capsys.readouterr()).err.split("\n")
    assert "Error: time input '' does not match format MM-DD-YYYY" in all_outputs
    assert "Error: time input 'Characters' does not match format MM-DD-YYYY" in all_outputs
    assert "Error: time input ' 06-20-2000' does not match format MM-DD-YYYY" in all_outputs
    assert "Error: time input '06-20-2000 ' does not match format MM-DD-YYYY" in all_outputs
    assert time_string == "06-20-2000"