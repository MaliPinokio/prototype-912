import os

from bot import DiscordBot

def main():
    token = os.getenv('DISCORD_TOKEN')
    bot = DiscordBot()
    bot.run(token)

if __name__ == '__main__':
    main()