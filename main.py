import discord
import random
import asyncio
import logging

# Setup logging for console output
logging.basicConfig(level=logging.INFO, format="%(message)s")

# Load tokens from tokens.txt
with open("tokens.txt", "r") as f:
    TOKENS = [line.strip() for line in f if line.strip()]

# Your target server and channel IDs
GUILD_ID = 123456789012345678  # Replace with your server ID
CHANNEL_ID = 123456789012345678  # Replace with your channel ID

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
        super().__init__()
        self.token = token

    async def on_ready(self):
        logging.info(f"\033[92mSuccess -=> logged in {self.token[:5]}...")  # Green color output
        await self.start_chat()

    async def on_message(self, message):
        if message.author.bot:
            return  # Ignore bot messages
        
        if message.channel.id == CHANNEL_ID:
            response = random.choice(MESSAGES)
            await message.channel.send(response)

    async def start_chat(self):
        await asyncio.sleep(random.randint(5, 15))  # Random delay to look more natural
        channel = self.get_channel(CHANNEL_ID)
        if channel:
            while True:
                await channel.send(random.choice(MESSAGES))
                await asyncio.sleep(random.randint(20, 60))  # Chat interval

# Start multiple bots
bots = []
for token in TOKENS:
    bot = ChatBot(token)
    bots.append(bot)
    bot.run(token, bot=False)  # `bot=False` for self-bots
        
