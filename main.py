import discord
import asyncio
import random
import logging
from colorama import Fore, Style, init

# Initialize colorama for colored console output
init(autoreset=True)

# Configure logging
logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")

# Load tokens
with open("tokens.txt", "r") as f:
    TOKENS = [line.strip() for line in f.readlines() if line.strip()]

# Server and channel settings (Edit in main.py)
GUILD_ID = 123456789012345678  # Replace with your server ID
CHANNEL_ID = 987654321098765432  # Replace with your channel ID

# Hinglish AI-style messages
HINGLISH_RESPONSES = [
    "Haan bhai, kya scene hai?", "Mujhe laga tu busy hoga.", "Kuch naya bata!", 
    "Sahi baat hai!", "Mast mast, or kya chal raha hai?", "Bhai, tu kya soch raha hai?", 
    "Arey waah! Yeh toh next level hai.", "Bhai OP!", "Koi tension nahi, sab badhiya hai!"
]

class HinglishChatBot(discord.Client):
    def __init__(self, token):
        intents = discord.Intents.default()
        intents.messages = True
        intents.guilds = True
        intents.message_content = True
        super().__init__(intents=intents)
        self.token = token

    async def on_ready(self):
        print(f"{Fore.GREEN}Success -=> Logged in {self.user}{Style.RESET_ALL}")
        logging.info(f"Connected as {self.user}")
        guild = self.get_guild(GUILD_ID)
        if guild:
            logging.info(f"Connected to server: {guild.name}")
        else:
            logging.warning(f"Could not find server with ID {GUILD_ID}")

    async def on_message(self, message):
        if message.author == self.user or message.channel.id != CHANNEL_ID:
            return  # Ignore self-messages and messages outside the target channel
        
        if random.random() < 0.5:  # 50% chance to reply
            await asyncio.sleep(random.randint(3, 8))  # Delay for realism
            response = random.choice(HINGLISH_RESPONSES)
            await message.channel.send(response)
            logging.info(f"{self.user} replied in {message.channel.name}: {response}")

    async def start_bot(self):
        try:
            await self.start(self.token)
        except Exception as e:
            logging.error(f"Error with token {self.token[:5]}...: {e}")

async def main():
    tasks = []
    for token in TOKENS:
        bot = HinglishChatBot(token)
        tasks.append(bot.start_bot())

    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
