import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

prefix = os.getenv('PREFIX')

bot = commands.Bot(command_prefix=prefix)

bot.load_extension("cogs.maincog")

TOKEN = os.getenv('DISCORD_TOKEN')

bot.run(TOKEN)