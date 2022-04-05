import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json, asyncio, datetime

class 經驗值系統(Cog_Extension):

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content != '' and msg.author != self.bot.user:
            now_time = datetime.datetime.now().strftime('%y%m%d%H%M')
            sever_member_id = []
            sever_member = []
            xp = []
            level = []
            xp_cold_time = []
            with open('data.json','r',encoding='utf8') as jfile:
                jdata = json.load(jfile)
            sever_member_id = jdata['sever_member_id']
            sever_member = jdata['sever_member']
            xp = jdata['xp']
            level = jdata['level']
            xp_cold_time = jdata["xp_cold_time"]

            if msg.author.id not in sever_member_id:
                sever_member_id.append(msg.author.id)
                sever_member.append(msg.author.name)
                xp.append(0)
                level.append(0)
                xp_cold_time.append(0)
            else:
                sever_member[sever_member_id.index(msg.author.id)] = msg.author.name
            
            if (int(now_time) - int(xp_cold_time[sever_member_id.index(msg.author.id)])) >= 2:
                xp[sever_member_id.index(msg.author.id)] += 1
                xp_cold_time[sever_member_id.index(msg.author.id)] = now_time

            if xp[sever_member_id.index(msg.author.id)] >= (level[sever_member_id.index(msg.author.id)] + 1) ** 2:
                xp[sever_member_id.index(msg.author.id)] = 0
                level[sever_member_id.index(msg.author.id)] += 1
                embed=discord.Embed(title=f'你升到了 Level {level[sever_member_id.index(msg.author.id)]} !', color=0x5560f3)
                embed.set_author(name=msg.author.name, icon_url=msg.author.avatar_url)
                await msg.channel.send(embed=embed)
            
            jdata['sever_member_id'] = sever_member_id
            jdata['sever_member'] = sever_member
            jdata['xp'] = xp
            jdata['level'] = level
            jdata["xp_cold_time"] = xp_cold_time
            with open('data.json','w',encoding='utf8') as jfile:
                    json.dump(jdata,jfile,indent=4)

    @commands.command()
    async def check_level(self, ctx):
        with open('data.json','r',encoding='utf8') as jfile:
            jdata = json.load(jfile)
        sever_member_id = jdata['sever_member_id']
        xp = jdata['xp']
        level = jdata['level']
        embed=discord.Embed(title=" ", color=0x5560f3)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.add_field(name="Level", value=level[sever_member_id.index(ctx.author.id)], inline=True)
        embed.add_field(name="XP", value=xp[sever_member_id.index(ctx.author.id)], inline=True)
        await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(經驗值系統(bot))