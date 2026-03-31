from get_tarot import get_random_card, parse_response, format_dict

def main():
    # As MVP I am only getting one random card, function default, eventually prompting for multiple?
    [selected_card] = parse_response(get_random_card()) # Unpacking list with only one card dict

    return format_dict(selected_card)


if __name__ == "__main__":
    main()