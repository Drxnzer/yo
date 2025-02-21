import discord
import random
import asyncio
import openai
import logging
from colorama import Fore, Style

# OpenAI API Key (Replace with your secure key)
openai.api_key = "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"

# Load tokens from tokens.txt
with open("tokens.txt", "r") as f:
    TOKENS = [line.strip() for line in f if line.strip()]

# Your target server and channel IDs
GUILD_ID = 1106443900127805470  # Replace with your server ID
CHANNEL_ID = 1340673021530345502  # Replace with your channel ID

# Logging setup
logging.basicConfig(level=logging.INFO, format="%(message)s")

class ChatBot(discord.Client):
    def __init__(self, token):
        super().__init__(intents=discord.Intents.default())
        self.token = token

    async def on_ready(self):
        logging.info(f"{Fore.BLUE}Fetched channel and server data!{Style.RESET_ALL}")
        logging.info(f"{Fore.GREEN}Success -=> logged in {self.token[:5]}...{Style.RESET_ALL}")
        await self.start_chat()

    async def on_message(self, message):
        if message.author.bot:
            return  # Ignore bot messages

        if message.channel.id == CHANNEL_ID:
            response = await self.generate_ai_response(message.content)
            await asyncio.sleep(random.uniform(1, 2))  # Random delay before response
            await message.channel.send(response)

    async def start_chat(self):
        logging.info(f"{Fore.MAGENTA}Chatting Started!{Style.RESET_ALL}")
        channel = self.get_channel(CHANNEL_ID)
        if channel:
            while True:
                message = await self.generate_ai_response("Chat something")
                await channel.send(message)
                await asyncio.sleep(random.uniform(20, 60))  # Random chat interval

    async def generate_ai_response(self, user_input):
        """Generate AI response in Hinglish using OpenAI API"""
        prompt = f"You are an AI chatting in Hinglish (Hindi in English alphabets). Respond naturally.\n\nUser: {user_input}\nAI:"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"]

# Start multiple bots
bots = []
for token in TOKENS:
    bot = ChatBot(token)
    asyncio.create_task(bot.start(token))  # Run all bots asynchronously

asyncio.run(asyncio.sleep(999999))  # Keep script running
