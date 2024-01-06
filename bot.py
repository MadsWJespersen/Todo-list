import discord
import os

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

intents = discord.Intents.default()
intents.reactions = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    await message.add_reaction('👍')

@bot.event
async def on_reaction_add(reaction, user):
    if reaction.emoji == '👍' and user != bot.user:
        await reaction.message.delete()

bot.run(os.getenv('TOKEN'))