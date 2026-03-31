import pytest
import json
from get_tarot import get_random_card


with open("test_card.json") as f:
    test_card_set = json.load(f)

with open("test_card_set.json") as f:
    test_card = json.load(f)


def test_wrong_number():
    with pytest.raises(ValueError):
        get_random_card(0)