import pytest
import json
import sys
from get_tarot import get_random_card, parse_response, construct_url, format_dict_to_list, format_dict_to_str
from pathlib import Path

test_dir = Path(__file__).parent
sys.path.append("../")

# Test data:
with open("card.json") as f:
    card = json.load(f)

with open("card_set.json") as f:
    card_set = json.load(f)

with open("card_faulty.json") as f:
    card_faulty = json.load(f)


# Random card API:
def test_output_format():
    assert isinstance(get_random_card(), dict)

def test_response_format():
    assert list(get_random_card().keys()) == ["nhits", "cards"]

@pytest.mark.parametrize("key", ["name", "desc", "meaning_up", "meaning_rev"])
def test_response_card_data(key):
    response = get_random_card()["cards"][0]
    assert key in response.keys()

def test_wrong_number():
    with pytest.raises(ValueError):
        get_random_card(0)

def test_wrong_datatype():
    with pytest.raises(ValueError):
        get_random_card("one")


# Parsing:
def test_parse_correct_output_type():
    assert isinstance(parse_response(card), list)

def test_parse_correct_output_key():
    expected_keys = {"name", "description", "orientation", "meaning", "link"}
    assert parse_response(card)[0].keys() == expected_keys

def test_parse_correct_output_value():
    assert parse_response(card)[0]["name"] == "Four of Wands"

def test_parse_no_input():
    with pytest.raises(TypeError):
        parse_response()

def test_parse_wrong_input():
    with pytest.raises(ValueError):
        parse_response(["card", "name"])

def test_parse_missing_key():
    with pytest.raises(KeyError):
        parse_response(card_faulty)


# Formatting:
sample_dict = {"name": "Alice", "age": 45}

def test_format_list():
    assert format_dict_to_list(sample_dict) == [['Name','Alice'], ['Age', 45]]

def test_format_str():
    assert format_dict_to_str(sample_dict) == "Name: Alice\nAge: 45"

