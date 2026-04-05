import pytest
import json
import sys
from get_tarot import get_random_card, parse_response

sys.path.append("../")

# Test data:
with open("test_card.json") as f:
    test_card = json.load(f)

with open("test_card_set.json") as f:
    test_card_set = json.load(f)

with open("test_card_faulty.json") as f:
    test_card_faulty = json.load(f)


# Random card API:
def test_wrong_number():
    with pytest.raises(ValueError):
        get_random_card(0)
        
        
def test_wrong_datatype():
    with pytest.raises(ValueError):
        get_random_card("one")


# Parsing:
def test_correct_output_type():
    assert isinstance(parse_response(test_card), list)

def test_correct_output_key():
    expected_keys = {"name", "description", "orientation", "meaning", "link"}
    assert parse_response(test_card)[0].keys() == expected_keys
    
def test_correct_output_value():
    assert parse_response(test_card)[0]["name"] == "Four of Wands"
    
def test_no_input():
    with pytest.raises(TypeError):
        parse_response()

def test_wrong_input():
    with pytest.raises(ValueError):
        parse_response(["card", "name"])
    
def test_missing_key():
    with pytest.raises(KeyError):
        parse_response(test_card_faulty)


# URL: