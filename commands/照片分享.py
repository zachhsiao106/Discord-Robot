import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random, json

with open('data.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class 照片分享(Cog_Extension):

    @commands.command(name="召喚七海小天使", help="可以召喚七海小天使")
    async def 召喚七海小天使(self, ctx):
        random_picture = random.choice(jdata['ChiakiNanami_picture'])
        picture = discord.File(random_picture)
        await ctx.send(file= picture)
    
    @commands.command(name="Weiwifu", help="可以召喚 Wei 的老婆")
    async def Weiwifu(self, ctx):
        if str(ctx.author.name) == 'Wei':
            random_picture = random.choice(jdata['Wei_picture'])
            await ctx.send(random_picture)
        else:
            random_picture = random.choice(jdata['Wei_picture'])
            await ctx.send(random_picture)
            await ctx.send(f'{ctx.author.mention} 照片可以看，但請不要變得跟 Wei 一樣油!')
    
    @commands.command(name="add_Weiwifu", help="可以新增 Wei 的老婆(Wei 限定)")
    async def add_Weiwifu(self, ctx, website:str):
        Wei_picture = []
        with open('data.json','r',encoding='utf8') as jfile:
            jdata = json.load(jfile)
        Wei_picture = jdata['Wei_picture']
        if website in Wei_picture and str(ctx.author.name) == 'Wei':
            await ctx.send(f'{ctx.author.mention} 這張照片重複放過了!')
        elif website[:4] == 'http' and str(ctx.author.name) == 'Wei':
            Wei_picture.append(website)
            jdata['Wei_picture'] = Wei_picture
            with open('data.json','w',encoding='utf8') as jfile:
                json.dump(jdata,jfile,indent=4)
            await ctx.send(f'{ctx.author.mention} 照片處存成功!')
        elif website[:4] != 'http' and str(ctx.author.name) == 'Wei':
            await ctx.send(f'{ctx.author.mention} 這不是照片的連結!')
        else:
            await ctx.send("你不是 Wei，不要存一些不油的東西在裡面!")

def setup(bot):
    bot.add_cog(照片分享(bot))