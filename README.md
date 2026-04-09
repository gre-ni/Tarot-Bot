# Discord Tarot Bot

A simple message bot which draws and shows a random tarot card when prompted with `!tarot` command in a Discord channel. It uses open source API [tarotapi.dev](https://tarotapi.dev/) and also provides a link to [biddytarot](https://biddytarot.com/tarot-card-meanings/), a popular tarot website, in case the user wants to read a little more about their card!

![image-discord-bot](./media/discord-bot-readme.png)

## Add to Your Server

[Link to invite the bot](https://discord.com/oauth2/authorize?client_id=1488647188430065835&permissions=274877975552&integration_type=0&scope=bot)

Once added, you can use the `!tarot` command in any channel or thread.

The bot has following permissions: view channels, send messages, send messages in threads and view message history

## Hosting Your Own Instance

### Prerequisites

- Python 3.10+
- A Discord bot token: ([can be generated here](https://discord.com/developers/applications))

### Setup

```bash
# Clone the repo
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name

# Virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Dependencies
pip install -r requirements.txt

# Create a .env file with your token, provided by Discord, see above
echo "DISCORD_KEY=your_token_here" > .env

# Run the bot
python main.py
```

Optionally, you can run the `print_card()` function in main to test tabulated output printed into terminal.

## How It Works

When `!tarot` is called, the bot:

1. Makes a GET request to the Tarot API for a random card
2. Randomly assigns upright or reversed orientation and selects the matching meaning
3. Constructs a URL to the card's page on Biddy Tarot
4. Returns a formatted message with name, description, orientation, meaning, and link

### Project Structure

```
project/
├── tests/
│   ├── card.json           # sample response
│   ├── card_faulty.json    # malformed response for error testing
│   ├── card_set.json
│   ├── test_get_tarot.py
│   └── __init__.py
├── main.py                 # launch from here
├── get_tarot.py            # API request, parsing, URL construction
├── bot.py                  # bot instance run
├── requirements.txt
└── .env
```

## Planned Improvements

- At the moment, I am relying on a specific API and biddytarot URL format → if those change or stop working, the bot will break. Since the card deck is limited and static, it would be better to migrate to a database in the future.
- Introduce async handling also for the API calls, in case the usage spikes.
- Improve testing structure: Use mocks for unit testing API calls and Discord client.
- Add the option of selecting multiple cards at once (current implementation is set up to allow for that scaling, return value of getting/parsing a card is a list by default)

## What I Learned

- Improve my error handling habits: I've learned how exceptions travel up the call stack, where to raise vs. catch them, and how to pass useful context through error objects
- I started working in isolated virtual environments per project rather than system-level Python, managing dependencies
- Deployment: moving a local project to a cloud server, working with environment variables on a platform (Railway), and understanding the difference between local dev setup and a production environment
- Unit testing randomised output and mock testing
