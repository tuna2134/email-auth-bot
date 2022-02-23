from discord.ext import commands
import discord

intents = discord.Intents.All()
bot = commands.Bot(command_prefix="ea!", intents=intents)

@bot.event
async def on_ready():
    print("起動じゃ")
    bot.dispatch("full_ready")
    
bot.run()
