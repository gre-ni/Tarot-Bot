import requests
import json
import random
from tabulate import tabulate


def draw_card(n: int=1):
    # As MVP I am only getting one random card, function default, eventually prompting for multiple?
    [selected_card] = parse_response(get_random_card(n)) # Unpacking list with only one card dict

    return format_dict_to_str(selected_card)


def print_card(n: int=1):
    # Just one card
    [selected_card] = parse_response(get_random_card())
    
    print(tabulate(format_dict_to_list(selected_card), tablefmt="plain"))
    


def get_random_card(n: int = 1):
    if n not in range(1, 79):
        raise ValueError(f"Provide a number between 1-78")
        
    try:
        result = requests.get("https://tarotapi.dev/api/v1/cards/random", params={"n": n})
        return result.json()
    except requests.RequestException as e:
        raise RuntimeError(f"Failed to reach the Tarot API: {e}")


def parse_response(info: dict) -> list:
    '''This function selects only relevant information from API body and picks orientation at random'''
    parsed_cards = []
    
    if not isinstance(info,dict):
        raise ValueError("Parse expects dictionary input.")
    
    cards = info["cards"]
    try:
        for card in cards:
            parsed_card = {}
            parsed_card["name"] = card["name"]
            parsed_card["description"] = card["desc"]
            parsed_card["orientation"] = random.choice(["Upright", "Reversed"])
            if parsed_card["orientation"] == "Upright":
                parsed_card["meaning"] = card["meaning_up"]
            else:
                parsed_card["meaning"] = card["meaning_rev"]
            parsed_cards.append(parsed_card)
            parsed_card["link"] = construct_url(card)
            
        return parsed_cards
    
    except KeyError as e:
        raise ValueError(f"Unexpected API response format, missing field: {e}")


def format_dict_to_str(input: dict) -> str:
    return "\n".join(f"{k.title()}: {v}" for k, v in input.items())

# Reformat to list of list to use tabulate on for printing to terminal:
def format_dict_to_list(input: dict) -> list:
    list_format = []
    for k, v in input.items():
        list_format.append([k.title(), v])
    return list_format


# https://biddytarot.com/tarot-card-meanings/major-arcana/hermit
# https://biddytarot.com/tarot-card-meanings/minor-arcana/suit-of-cups/two-of-cups/

def construct_url(card: dict) -> str:
    url = "https://biddytarot.com/tarot-card-meanings"
    type = card["type"]
    if type == "minor":
        value = card["value"]
        suit = card["suit"]
        return f"{url}/{type}-arcana/suit-of-{suit}/{value}-of-{suit}/"
    elif type == "major":
        name = card["name"].replace("The ", "").replace(" ", "-").lower()
        return f"{url}/{type}-arcana/{name}/"        
    else:
        raise ValueError

    