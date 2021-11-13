import discord
from discord.ext import commands

bot = commands.Bot(command_prefix= '/')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(877085946263265313)
    await channel.send(f'{member} join!')


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(877085946263265313)
    await channel.send(f'{member} leave!')

bot.run('ODk4OTc4MDc4NDAxODk2NTY5.YWsElA.5CIB5gqF6WzQcyFISyOvsM25b_g')