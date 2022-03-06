import asyncio
import datetime

import discord
from discord.ext import commands

from utils.async_thread import AsyncThread
from cogs.simple_cog import SimpleCog

CHANNEL_DOESNT_EXIST_ERROR_MESSAGE = \
    'Selected channel doesn\'t exist.'
CHANNEL_NOT_IN_SERVER_ERROR_MESSAGE = \
    'Selected channel is not in this server.'

class UTCChanelName(SimpleCog):
    """ Enables functionality to periodically update names
        of selected channels with current UTC time 
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__update_thread = AsyncThread(
            target=self.channel_update_loop
        )
        
    @commands.Cog.listener()
    async def on_ready(self):
        self.__update_thread.start()

    @commands.command()
    async def utcname(self, ctx, num):
        ctx_channel = ctx.guild
        selected_channel = self.client.get_channel(int(num))
        if not selected_channel:
            await self.client.reply(
                ctx, CHANNEL_DOESNT_EXIST_ERROR_MESSAGE, 60, True)
        elif ctx_channel != selected_channel:
            await self.client.reply(
                ctx, CHANNEL_NOT_IN_SERVER_ERROR_MESSAGE, 60, True)
        else:
            pass

    async def channel_update_loop(self):
        while True:
            print('Check')
            await asyncio.sleep(60) # Wait a minute


def setup(bot):
    bot.add_cog(UTCChanelName(bot))
