import discord
import openai
import random
import asyncio
import logging
from colorama import Fore, init

# Initialize colorama for colored console output
init(autoreset=True)

# OpenAI API Key (Replace with your actual key)
OPENAI_API_KEY = "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"  # Replace with your OpenAI API key
openai.api_key = OPENAI_API_KEY

# Load tokens from tokens.txt
with open("tokens.txt", "r") as f:
    TOKENS = [line.strip() for line in f if line.strip()]

# Your target server and channel IDs
GUILD_ID = 1106443900127805470  # Replace with your server ID
CHANNEL_ID = 1340673021530345502  # Replace with your channel ID

# Logging setup
logging.basicConfig(level=logging.INFO, format="%(message)s")

# AI Response Generation Function
async def generate_ai_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return "Mujhe samajh nahi aya!"

class SelfBot(discord.Client):
    def __init__(self, token):
        super().__init__(self, intents=discord.Intents.default())
        self.token = token

    async def on_ready(self):
        logging.info(f"{Fore.GREEN}Success -=> logged in {self.token[:5]}...")
        logging.info(f"{Fore.BLUE}Fetched channel and server data!")

        # Start chatting
        asyncio.create_task(self.start_chat())

    async def on_message(self, message):
        if message.author.bot:
            return  # Ignore bot messages

        if message.channel.id == CHANNEL_ID:
            ai_response = await generate_ai_response(message.content)
            await asyncio.sleep(random.uniform(1.5, 3.0))  # Delay to mimic typing
            await message.channel.send(ai_response)

    async def start_chat(self):
        await asyncio.sleep(random.randint(5, 15))  # Initial delay
        channel = self.get_channel(CHANNEL_ID)

        if channel:
            logging.info(f"{Fore.MAGENTA}Chatting Started!")
            while True:
                ai_message = await generate_ai_response("Say something in Hinglish.")
                await channel.send(ai_message)
                await asyncio.sleep(random.uniform(30, 90))  # Random interval between messages

    def run_self_bot(self):
        self.run(self.token, bot=False)  # Running as a self-bot

# Start multiple self-bots
for token in TOKENS:
    bot = SelfBot(token)
    asyncio.create_task(bot.run_self_bot())

# Run event loop
asyncio.get_event_loop().run_forever()

