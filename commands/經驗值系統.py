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
        sever_member_id = []
        xp = []
        level = []
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
    
    @commands.command()
    async def check_level_leader(self, ctx):
        leader = ""
        level_and_xp = ""
        No = ""
        temp_str = ""
        temp_int = 0
        sever_member = []
        xp = []
        level = []
        with open('data.json','r',encoding='utf8') as jfile:
            jdata = json.load(jfile)
        sever_member = jdata['sever_member']
        xp = jdata['xp']
        level = jdata['level']

        for i in range(len(level) - 1):
            for j in range(len(level) - i - 1):
                if level[j] < level[j+1]:
                    temp_int = level[j]
                    level[j] = level[j+1]
                    level[j+1] = temp_int
                    temp_int = xp[j]
                    xp[j] = xp[j+1]
                    xp[j+1] = temp_int
                    temp_str = sever_member[j]
                    sever_member[j] = sever_member[j+1]
                    sever_member[j+1] = temp_str
                elif level[j] == level[j+1]:
                    if xp[j] < xp[j+1]:
                        temp_int = xp[j]
                        xp[j] = xp[j+1]
                        xp[j+1] = temp_int
                        temp_str = sever_member[j]
                        sever_member[j] = sever_member[j+1]
                        sever_member[j+1] = temp_str

        for k in range(len(level)):
            No += f'No.{k + 1}\n'
            leader += f'{sever_member[k]}\n'
            level_and_xp += f'Level:{level[k]} Xp:{xp[k]}\n'
        embed=discord.Embed(title="經驗排行榜", color=0x1ed760)
        embed.add_field(name="名次", value=No, inline=True)
        embed.add_field(name="名稱", value=leader, inline=True)
        embed.add_field(name="Level & Xp", value=level_and_xp, inline=True)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(經驗值系統(bot))