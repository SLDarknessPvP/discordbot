import discord
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')
Channel_ID = config.get('wolfbitez', 'Channel')
Token_ID = config.get('wolfbitez', 'Token')
dclient = discord.Client()
@dclient.event
async def on_ready():
    await dclient.change_presence(game=discord.Game(name=config.get('wolfbitez', 'Playing')))
    if Channel_ID != 0:
        await dclient.send_message(discord.Object(id=Channel_ID), "no")
dclient.run(Token_ID)
