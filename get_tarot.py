import requests
import json

def get_random_card(n: int = 1):
    if n not in range(1, 79):
        raise ValueError(f"Provide a number between 1-78")
        
    try:
        result = requests.get("https://tarotapi.dev/api/v1/cards/random", params={"n": n})
        return result.json()
    except requests.RequestException:
        raise