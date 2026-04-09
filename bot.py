import os
import discord
import traceback
from dotenv import load_dotenv
from get_tarot import draw_card

load_dotenv()

def launch_bot():
    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'We have logged in as {client.user}')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('!tarot'):
            try:
                await message.channel.send(draw_card())
            except Exception as e:
                print(f"Error in !tarot command: {e}")
                traceback.print_exc()
                await message.channel.send("🔮 The oracle is asleep right now, try again later.")

    client.run(os.getenv("DISCORD_KEY"))