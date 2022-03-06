import os
import asyncio

import discord
from discord.ext import commands

class DiscordBot(commands.Bot):
    """ Class defining bot logic and behaviour """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load_cogs()

    async def on_ready(self):
        print('Logged in as', self.user)

    def load_cogs(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        cogs_path = os.path.join(dir_path, 'cogs/implementations')
        cog_filenames = os.listdir(cogs_path)
        for filename in cog_filenames:
            if filename.endswith('py'):
                self.load_extension(
                    f'cogs.implementations.{filename[:-3]}')

    async def set_playing_activity(self, activity):
        """ Changes text 'Playing ...' under bot's name on Discord """
        await self.change_presence(activity=discord.Game(name=activity))

    async def reply(self, ctx, message, lifetime=None, 
            delete_ctx_message=False):
        """ Replying to context with message and deleting the reply
            after lifetime given in seconds (no deletion 
            if lifetime is None). Original message can be deleted
            by passing True for value of parameter delete_ctx_message
        """
        message = await ctx.reply(message)
        if delete_ctx_message:
            await ctx.message.delete()
        if lifetime:
            await asyncio.sleep(lifetime)
            await message.delete()
    
