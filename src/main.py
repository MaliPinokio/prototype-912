import os
import logging

from bot import DiscordBot

from data.engine_utils import get_engine

logging.basicConfig(level=logging.INFO)

def main():
    token = os.getenv('DISCORD_TOKEN')
    database_url = os.getenv('DATABASE_URL')
    engine = get_engine(database_url)
    bot = DiscordBot(
        command_prefix='~', self_bot=False)
    bot.run(token)

if __name__ == '__main__':
    main()