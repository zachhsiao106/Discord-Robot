import discord
from discord.ext import commands
import json
import random
import os

with open('data.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix= '~',intents = intents)

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.command()
async def load(ctx, extension):
    bot.load_extension(F'commands.{extension}')
    await ctx.send(F'下載 {extension} 完畢!')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(F'commands.{extension}')
    await ctx.send(F'卸載 {extension} 完畢!')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(F'commands.{extension}')
    await ctx.send(F'重新載入 {extension} 完畢!')

for Filename in os.listdir('./commands'):
    if Filename.endswith('.py'):
        bot.load_extension(F'commands.{Filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])