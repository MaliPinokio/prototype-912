import discord
from discord.ext import commands

class DiscordBot(commands.Bot):
    """ Class defining bot logic and behaviour """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load_cogs()

    async def on_ready(self):
        print('Logged on as', self.user)

    def load_cogs(self):
        import os
        for filename in os.listdir('./cogs/implementations'):
            if filename.endswith('py'):
                self.load_extension(
                    f'cogs.implementations.{filename[:-3]}')

    async def set_playing_activity(self, activity):
        """ Changes text 'Playing ...' under bot's name on Discord """
        await self.change_presence(activity=discord.Game(name=activity))