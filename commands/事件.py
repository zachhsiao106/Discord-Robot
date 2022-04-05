import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('data.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class 事件(Cog_Extension):
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata['公告']))
        await channel.send(f'歡迎魯蛇 {member.mention} 加入!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata['公告']))
        await channel.send(f'魯蛇 {member.mention} 再見!')

def setup(bot):
    bot.add_cog(事件(bot))