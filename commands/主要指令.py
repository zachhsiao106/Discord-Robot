import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime, random


class 主要指令(Cog_Extension):

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'機器人延遲:{round(self.bot.latency*1000)} ms')

    @commands.command()
    async def update(self, ctx):
        embed=discord.Embed(title="更新布告欄", description="重大更新!", color=0xf1c7c7, timestamp= datetime.datetime.utcnow())
        embed.set_author(name="zachhsiao106", icon_url="https://i.imgur.com/o4qf13Qh.jpg")
        embed.set_thumbnail(url="https://pic.pimg.tw/mutsumi326/1468586958-4121451968_n.jpg")
        embed.add_field(name="#你可以用 ~help 來查詢指令!", value= "「~help」", inline=False)
        embed.add_field(name="#你可以用 ~say 來讓機器人說話", value= "「~say (要說的話)」", inline=False)
        embed.add_field(name="#你可以用 ~clean 來讓機器人刪除訊息", value= "「~clean (刪除訊息數量)」", inline=False)
        embed.add_field(name="#新功能：可以從 Discord 端進行 下載/卸載/重新載入", value="「下載：~load (功能名稱)/卸載：~unload (功能名稱)/重新載入：~reload (功能名稱)」", inline=False)
        embed.add_field(name="#更新布告欄排版了!", value= "「這裡變得更漂亮!」", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def repeat(self, ctx, num:int, *,msg):
        if num > 10:
            await ctx.send(f'{ctx.author.mention} 逼..逼...逼 在..吵..就...送..你 600..秒...大....禮......包(請不要洗版伺服器)')
        elif int(num) >= 1:
            await ctx.message.delete()
            for x in range(int(num)):
                await ctx.send(msg)
        else:
            await ctx.send(f'{ctx.author.mention} 逼逼逼... 機....油....好...難...喝(格式錯誤)')
    
    @commands.command()
    async def say(self, ctx, *,msg):
        await ctx.message.delete()
        await ctx.send(msg)
    
    @commands.command()
    async def clean(self, ctx, number:int):
        await ctx.channel.purge(limit=number+1)
        await ctx.send(f'{ctx.author.mention} 剛剛刪除了' + str(number) + "條內容")
    
    @commands.command()
    async def detect_condition(self, ctx):
        for member in ctx.guild.members:
            if str(member.status) == 'online':
                await ctx.send(str(member.name) + " 正在線上")
            elif str(member.status) == 'offline':
                await ctx.send(str(member.name) + " 離線中")
            elif str(member.status) == 'idle':
                await ctx.send(str(member.name) + " 閒置中")
            elif str(member.status) == 'dnd':
                await ctx.send(str(member.name) + " 不想被打擾")
            elif str(member.status) == 'invisible':
                await ctx.send(str(member.name) + " 明明就在線上，還敢隱形")
    
    @commands.command()
    async def random_squad(self, ctx):
        online = []
        for member in ctx.guild.members:
            if str(member.status) == 'online' and member.bot == False:
                online.append(member.name)
        for squad in range(2):
            random_squad = random.sample(online, k=int(len(online)/2))
            await ctx.send(random_squad)
            for name in random_squad:
                online.remove(name)

def setup(bot):
    bot.add_cog(主要指令(bot))