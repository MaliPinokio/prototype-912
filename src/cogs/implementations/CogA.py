import asyncio
import datetime

import discord
from discord.ext import commands

from utils.async_thread import AsyncThread
from cogs.simple_cog import SimpleCog

class CogA(SimpleCog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__update_thread = AsyncThread(
            target=self.update_channels
        )

    @commands.Cog.listener()
    async def on_ready(self):
        self.__update_thread.start()
        print('CogA ready')

    @commands.command()
    async def status(self, ctx, num):
        print(num)
        await self.scheduler(num)

    async def update_channels(self):
        while True:
            print('Check')
            await asyncio.sleep(5)

def setup(bot):
    bot.add_cog(CogA(bot))
