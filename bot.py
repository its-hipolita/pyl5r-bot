import discord
import os
import re
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
BASE_URL = os.getenv('BASE_URL')  # Base URL for images hosted on Vercel

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    card_name_match = re.search(r'\[\[(.*?)\]\]', message.content)
    if card_name_match:
        card_name = card_name_match.group(1).strip()
        # Convert card name to filename (you may need to adjust this depending on your naming convention)
        filename = f"{card_name}.jpg"
        image_url = f"{BASE_URL}/images/cards/{filename}"

        embed = discord.Embed(title=card_name)
        embed.set_image(url=image_url)
        
        await message.channel.send(embed=embed)

    await bot.process_commands(message)

bot.run(TOKEN)
