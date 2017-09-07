import discord
from configparser import ConfigParser

# Reads the config file..
config = ConfigParser()
config.read('config.ini')

# Makes it easier to reference stuff from the config..
Channel_ID = config.get('wolfbitez', 'Channel')
Token_ID = config.get('wolfbitez', 'Token')

# Initialises the bot..
dclient = discord.Client()

# "Playing" function and startup message..
@dclient.event
async def on_ready():
    await dclient.change_presence(game=discord.Game(name=config.get('wolfbitez', 'Playing')))
    if Channel_ID != 0:
        await dclient.send_message(discord.Object(id=Channel_ID), "Successfully booted.")

# Runs the bot..
dclient.run(Token_ID)
