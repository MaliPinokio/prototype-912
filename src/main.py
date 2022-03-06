import os
import logging

from bot import DiscordBot

logging.basicConfig(level=logging.INFO)

def main():
    token = os.getenv('DISCORD_TOKEN')
    bot = DiscordBot(command_prefix='~', self_bot=False)
    bot.run(token)

if __name__ == '__main__':
    main()