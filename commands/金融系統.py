import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

class 金融系統(Cog_Extension):
    
    @commands.command()
    async def sign_up_bank_account(self, ctx):
        bank_account_id = []
        bank_account = []
        bank_money = []
        daily_check_in = []
        with open('data.json','r',encoding='utf8') as jfile:
            jdata = json.load(jfile)
        bank_account_id = jdata['bank_account_id']
        bank_account = jdata['bank_account']
        bank_money = jdata['bank_money']
        daily_check_in = jdata['daily_check_in']

        if ctx.author.id in bank_account_id:
            await ctx.send(f'{ctx.author.mention} 銀行帳戶已經申請過了!')
            bank_account[bank_account_id.index(ctx.author.id)] = ctx.author.name
            jdata['bank_account'] = bank_account
            with open('data.json','w',encoding='utf8') as jfile:
                json.dump(jdata,jfile,indent=4)
        else:
            bank_account.append(ctx.author.name)
            bank_money.append(0)
            bank_account_id.append(ctx.author.id)
            daily_check_in.append(1)
            jdata['bank_account_id'] = bank_account_id
            jdata['bank_account'] = bank_account
            jdata['bank_money'] = bank_money
            jdata['daily_check_in'] = daily_check_in
            with open('data.json','w',encoding='utf8') as jfile:
                json.dump(jdata,jfile,indent=4)
            await ctx.send(f'{ctx.author.mention} 銀行帳戶申請成功!')

    @commands.command()
    async def check_bank_account(self, ctx):
        bank_account_id = []
        bank_account = []
        bank_money = []
        with open('data.json','r',encoding='utf8') as jfile:
            jdata = json.load(jfile)
        bank_account_id = jdata['bank_account_id']
        bank_account = jdata['bank_account']
        bank_money = jdata['bank_money']

        if ctx.author.id in bank_account_id:
            bank_account[bank_account_id.index(ctx.author.id)] = ctx.author.name
            jdata['bank_account'] = bank_account
            with open('data.json','w',encoding='utf8') as jfile:
                json.dump(jdata,jfile,indent=4)
            await ctx.send(f'{ctx.author.mention} 目前你的銀行帳戶餘額為 {bank_money[bank_account_id.index(ctx.author.id)]} 元!')
        else:
            await ctx.send(f'{ctx.author.mention} 你沒有申請銀行帳戶!(申請帳戶請在伺服器裡打「~sign_up_bank_account」)!')

    @commands.command()
    async def make_money(self, ctx, money:int):
        bank_account_id = []
        bank_account = []
        bank_money = []
        with open('data.json','r',encoding='utf8') as jfile:
            jdata = json.load(jfile)
        bank_account_id = jdata['bank_account_id']
        bank_account = jdata['bank_account']
        bank_money = jdata['bank_money']

        if ctx.author.id in bank_account_id:
            if ctx.author.id == 730437942383870046:
                bank_account[bank_account_id.index(ctx.author.id)] = ctx.author.name
                jdata['bank_money'] = bank_money
                jdata['bank_account'] = bank_account
                bank_money[bank_account_id.index(ctx.author.id)] = bank_money[bank_account_id.index(ctx.author.id)] + money
                with open('data.json','w',encoding='utf8') as jfile:
                    json.dump(jdata,jfile,indent=4)
                await ctx.send(f'{ctx.author.mention} 成功賺取 {money} 元!')
            else:
                bank_account[bank_account_id.index(ctx.author.id)] = ctx.author.name
                jdata['bank_account'] = bank_account
                with open('data.json','w',encoding='utf8') as jfile:
                    json.dump(jdata,jfile,indent=4)
                await ctx.send(f'{ctx.author.mention} 請不要搞垮金融系統!')
        else:
            await ctx.send(f'{ctx.author.mention} 你沒有申請銀行帳戶!(申請帳戶請在伺服器裡打「~sign_up_bank_account」)!')
        
    @commands.command()
    async def give_money(self, ctx, money:int, *, bank_account_name):
        bank_account_id = []
        bank_account = []
        bank_money = []
        with open('data.json','r',encoding='utf8') as jfile:
            jdata = json.load(jfile)
        bank_account_id = jdata['bank_account_id']
        bank_account = jdata['bank_account']
        bank_money = jdata['bank_money']

        if ctx.author.id in bank_account_id:
            if bank_account_name in bank_account:
                if money > 0:
                    if ctx.author.name != bank_account_name:
                        if bank_money[bank_account_id.index(ctx.author.id)] >= money:
                            bank_account[bank_account_id.index(ctx.author.id)] = ctx.author.name
                            bank_money[bank_account_id.index(ctx.author.id)] = bank_money[bank_account_id.index(ctx.author.id)] - money
                            bank_money[bank_account.index(bank_account_name)] = bank_money[bank_account.index(bank_account_name)] + money
                            jdata['bank_account'] = bank_account
                            jdata['bank_money'] = bank_money
                            with open('data.json','w',encoding='utf8') as jfile:
                                json.dump(jdata,jfile,indent=4)
                            await ctx.send(f'{ctx.author.mention} 成功轉帳給 {bank_account_name} {money} 元!')
                        else:
                            bank_account[bank_account_id.index(ctx.author.id)] = ctx.author.name
                            jdata['bank_account'] = bank_account
                            with open('data.json','w',encoding='utf8') as jfile:
                                json.dump(jdata,jfile,indent=4)
                            await ctx.send(f'{ctx.author.mention} 你的餘額不足!')
                    else:
                        bank_account[bank_account_id.index(ctx.author.id)] = ctx.author.name
                        jdata['bank_account'] = bank_account
                        with open('data.json','w',encoding='utf8') as jfile:
                            json.dump(jdata,jfile,indent=4)
                        await ctx.send(f'{ctx.author.mention} 你耍了你自己!等一下,你做不到!(請不要給自己錢!)')
                else:
                    bank_account[bank_account_id.index(ctx.author.id)] = ctx.author.name
                    with open('data.json','w',encoding='utf8') as jfile:
                        jdata['bank_account'] = bank_account
                        json.dump(jdata,jfile,indent=4)
                    await ctx.send(f'{ctx.author.mention} 你耍了你自己!等一下,你做不到!(請不要給0元!)')
            else:
                bank_account[bank_account_id.index(ctx.author.id)] = ctx.author.name
                jdata['bank_account'] = bank_account
                with open('data.json','w',encoding='utf8') as jfile:
                    json.dump(jdata,jfile,indent=4)
                await ctx.send(f'{ctx.author.mention} 找不到 {bank_account_name} 這個銀行帳戶!(有可能是 {bank_account_name} 改名了,請打 {bank_account_name} 的舊名,或是 {bank_account_name} 沒有銀行帳戶)')
        else:
            await ctx.send(f'{ctx.author.mention} 你沒有申請銀行帳戶!(申請帳戶請在伺服器裡打「~sign_up_bank_account」)!')

    @commands.command()
    async def daily_check_in(self, ctx):
        bank_account_id = []
        bank_account = []
        bank_money = []
        daily_check_in = []
        with open('data.json','r',encoding='utf8') as jfile:
            jdata = json.load(jfile)
        bank_account_id = jdata['bank_account_id']
        bank_account = jdata['bank_account']
        bank_money = jdata['bank_money']
        daily_check_in = jdata['daily_check_in']

        if ctx.author.id in bank_account_id:
            if daily_check_in[bank_account_id.index(ctx.author.id)] == 1:
                bank_account[bank_account_id.index(ctx.author.id)] = ctx.author.name
                bank_money[bank_account_id.index(ctx.author.id)] = bank_money[bank_account_id.index(ctx.author.id)] + 50
                daily_check_in[bank_account_id.index(ctx.author.id)] = 0
                jdata['bank_account'] = bank_account
                jdata['bank_money'] = bank_money
                jdata['daily_check_in'] = daily_check_in
                with open('data.json','w',encoding='utf8') as jfile:
                    json.dump(jdata,jfile,indent=4)
                await ctx.send(f'{ctx.author.mention} 每日簽到成功!')
            else:
                bank_account[bank_account_id.index(ctx.author.id)] = ctx.author.name
                jdata['bank_account'] = bank_account
                with open('data.json','w',encoding='utf8') as jfile:
                    json.dump(jdata,jfile,indent=4)
                await ctx.send(f'{ctx.author.mention} 請等到明天領取!')
        else:
            await ctx.send(f'{ctx.author.mention} 你沒有申請銀行帳戶!(申請帳戶請在伺服器裡打「~sign_up_bank_account」)!')

def setup(bot):
    bot.add_cog(金融系統(bot))