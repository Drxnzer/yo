import discord
import random
import asyncio
import logging

# Setup logging for console output with colors
logging.basicConfig(level=logging.INFO, format="%(message)s")

# ANSI color codes
GREEN = "\033[92m"
BLUE = "\033[94m"
PINK = "\033[95m"
RESET = "\033[0m"

# Load tokens from tokens.txt
with open("tokens.txt", "r") as f:
    TOKENS = [line.strip() for line in f if line.strip()]

# Your target server and channel IDs
GUILD_ID = 1106443900127805470  # Replace with your server ID
CHANNEL_ID = 1340673021530345502  # Replace with your channel ID

# Messages to send
MESSAGES = [
    "Hey!",
    "Kaise ho?",
    "Wassup?",
    "Kya chal raha hai?",
    "Mujhe pucho kuch!",
    "Aaj ka din kaisa tha?",
    "Bas time pass ho raha hai",
]

class ChatBot(discord.Client):
    def __init__(self, token):
        intents = discord.Intents.default()
        intents.messages = True
        super().__init__(intents=intents)
        self.token = token

    async def on_ready(self):
        logging.info(f"{GREEN}Success -=> logged in {self.token[:5]}...{RESET}")  # Green color output
        
        # Fetch channel and server info
        guild = self.get_guild(GUILD_ID)
        channel = self.get_channel(CHANNEL_ID)

        if guild and channel:
            logging.info(f"{BLUE}Fetched channel and server data!{RESET}")  # Blue message

        await self.start_chat(channel)

    async def start_chat(self, channel):
        if channel:
            logging.info(f"{PINK}Chatting Started!{RESET}")  # Pink message
            while True:
                await asyncio.sleep(random.uniform(1, 2))  # Random delay between 1-2 seconds
                await channel.send(random.choice(MESSAGES))

# Start multiple bots
bots = []
for token in TOKENS:
    bot = ChatBot(token)
    bot.run(token)  # Self-bot mode enabled
