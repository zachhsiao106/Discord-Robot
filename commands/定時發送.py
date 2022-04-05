import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json, asyncio, datetime

class 定時發送(Cog_Extension):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.counter1 = 0
        async def daily_check_in_counter():
            await self.bot.wait_until_ready()
            while not self.bot.is_closed():
                now_time = datetime.datetime.now().strftime('%H%M')

                if now_time == "0000" and self.counter1 == 0:
                    daily_check_in = []
                    with open('data.json','r',encoding='utf8') as jfile:
                        jdata = json.load(jfile)
                    daily_check_in = jdata['daily_check_in']

                    for i in range(len(daily_check_in)):
                        self.channel = self.bot.get_channel(938699368238817320)
                        daily_check_in[i] = 1
                        await self.channel.send(str(id) + '更新完畢!')
                    with open('data.json','w',encoding='utf8') as jfile:
                        json.dump(jdata,jfile,indent=4)
                    jdata['daily_check_in'] = daily_check_in
                    self.counter1 = 1
                    await self.channel.send('更新完畢!')
                    await asyncio.sleep(1)
                
                elif now_time == '0000' and self.counter1 == 1:
                    await asyncio.sleep(1)
                    pass
                
                else:
                    self.counter1 = 0
                    await asyncio.sleep(1)
                    pass
        
        self.bg_task = self.bot.loop.create_task(daily_check_in_counter())

        self.counter2 = 0
        async def bot_birthday():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(938699368238817320)
            while not self.bot.is_closed():
                now_time = datetime.datetime.now().strftime('%m%d')

                if now_time == "0314" and self.counter2 == 0:
                    await self.channel.send('@everyone今天是我生日喔!')
                    await self.channel.send('https://cache.pttweb.cc/imgur/i1GBD7T/f/0d2a5dc0b7e5a6ab46f71eab01804d9f')
                    self.counter2 = 1
                    await asyncio.sleep(1)
                
                elif now_time == "0314" and self.counter2 == 1:
                    await asyncio.sleep(1)
                    pass

                else:
                    await asyncio.sleep(1)
                    self.counter2 = 0
                    pass
                
        self.bg_task = self.bot.loop.create_task(bot_birthday())

    @commands.command()
    async def set_time(self, ctx, time):
        with open('data.json','r',encoding='utf8') as jfile:
            jdata = json.load(jfile)
        with open('data.json','w',encoding='utf8') as jfile:
            json.dump(jdata,jfile,indent=4)
        jdata['time'] = time
        await ctx.send(f'{ctx.author.mention} 時間設定完畢!')
    

    
    #def __init__(self,*args,**kwargs):
        #super().__init__(*args,**kwargs)
        
        #async def interval():
            #await self.bot.wait_until_ready()
            #self.channel = self.bot.get_channel(int(jdata['公告']))
            #while not self.bot.is_closed():
                #await self.channel.send("Hi i;m running!")
                #await asyncio.sleep(5)

        #self.bg_task = self.bot.loop.create_task(interval())
    #@commands.command()
    #async def set_channel(self, ctx,ch:int):
        #self.channel = self.bot.get_channel(ch)
        #await ctx.send(f'Set Channel:{self.channel.mention}')

def setup(bot):
    bot.add_cog(定時發送(bot))
