import asyncio
import datetime

import discord
from discord.ext import commands

from utils.async_thread import AsyncThread
from cogs.simple_cog import SimpleCog

from data.model.utc_named_channel import UTCNamedChannel
from data.dao.utc_named_channel_dao import UTCNamedChannelDao

CHANNEL_DOESNT_EXIST_ERROR_MESSAGE = \
    'Selected channel doesn\'t exist.'
NO_UPDATE_RATE_ERROR_MESSAGE = \
    'You must select update rate'

class UTCChanelName(SimpleCog):
    """ Enables functionality to periodically update names
        of selected channels with current UTC time 
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.utc_named_channel_dao = UTCNamedChannelDao()
        
    @commands.Cog.listener()
    async def on_ready(self):
        await self.channel_update_loop()

    @commands.command()
    async def utcname(self, ctx, channel_id, update_rate=None):
        channel_id = int(channel_id)
        selected_channel = self.client.get_channel(channel_id)
        if not selected_channel:
            await self.client.reply(
                ctx, CHANNEL_DOESNT_EXIST_ERROR_MESSAGE, 60, True)
        elif not update_rate:
            await self.client.reply(
                ctx, NO_UPDATE_RATE_ERROR_MESSAGE, 60, True)
        else:
            update_rate = max(0, int(update_rate))
            self.utc_named_channel_dao.add_channel(
                channel_id, update_rate
            )
            await self.client.reply(
                ctx, 'UTC named channel has been set successfully', None, True)

    async def channel_update_loop(self):
        while True:
            channels = self.utc_named_channel_dao.get_all()
            print(channels)
            time = datetime.datetime.utcnow()
            time_s = 'Server time(UTC): ' + time.strftime("%H:%M")
            for channel in channels:
                if time.minute % channel.update_rate == 0:
                    discord_channel = self.client\
                        .get_channel(channel.channel_id)
                    if discord_channel:
                        await discord_channel.edit(name=time_s)
            await asyncio.sleep(60) # Wait a minute

def setup(bot):
    bot.add_cog(UTCChanelName(bot))
