import discord

class DiscordBot(discord.Client):
    """ Class defining bot logic and behaviour """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    async def on_ready(self):
        print('Logged on as', self.user)