from get_tarot import get_random_card
import json

def main():
    print(get_random_card())
    print(json.dumps(get_random_card(2), indent=2))
    
if __name__ == "__main__":
    main()