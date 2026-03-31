from get_tarot import get_random_card, parse_response, format_dict
import json

def main():
    amount = 1 # As MVP I am only getting one random card
    [selected_card] = parse_response(get_random_card(amount)) # Unpacking list with only one card dict

    print(format_dict(selected_card))


if __name__ == "__main__":
    main()