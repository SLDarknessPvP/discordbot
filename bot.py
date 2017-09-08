import os
import sys
from configparser import ConfigParser
import discord
from discord import opus

# Imports Opus Libs
OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll']

def load_opus_lib(opus_libs=OPUS_LIBS):
    if opus.is_loaded():
        return True

    for opus_lib in opus_libs:
        try:
            opus.load_opus(opus_lib)
            return
        except OSError:
            pass
    raise RuntimeError('Could not load an opus lib. Tried %s' % (', '.join(opus_libs)))

# Reads the config
config = ConfigParser()
config.read('config.ini')

# Defines stuff from the config
cmd_char = config.get('wolfbitez', 'Command')
Channel_ID = config.get('wolfbitez', 'Channel')
Token_ID = config.get('wolfbitez', 'Token')
bot_name = config.get('wolfbitez', 'Name')
fileformat = config.get('wolfbitez', 'File Format')

dclient = discord.Client()

# Loads the playing status
@dclient.event
async def on_ready():
    await dclient.change_presence(game=discord.Game(name=config.get('wolfbitez', 'Playing')))
    if Channel_ID != 0:
        await dclient.send_message(discord.Object(id=Channel_ID), "Successfully booted.")

# The bots main function
@dclient.event
async def on_message(msg):
    if msg.author.id != dclient.user.id:
        if msg.content.startswith(cmd_char):
            userinput = msg.content.lower().replace(cmd_char, "")
            if userinput == 'help':
                g_4 = '\n' + cmd_char
                g_3 = '{0}git\n{0}{1}'.format(
                    cmd_char, g_4.join(os.listdir('music/')))
                g_3 = g_3.lower().replace(fileformat, '')
                g_2 = 'Commands for ' + bot_name + ':\n' + \
                    g_3 + '\nYou must be in a voice channel for this command to work.'
                if not msg.channel.is_private:
                    await dclient.send_message(msg.channel, 'Help has been sent to your DMs..')
                await dclient.send_message(msg.author, g_2)
            elif userinput == 'info':
                await dclient.send_message(msg.channel, 'I\'m a fairly simple bot coded in Python by wolfbitez. You can find his GitHub here: https://github.com/wolfbitez/discordbot/')
            else:
                if msg.author.voice_channel:
                    try:
                        voice = await dclient.join_voice_channel(msg.author.voice_channel)
                        player = voice.create_ffmpeg_player('music/' + userinput + fileformat)
                        player.start()
                    except:
                        pass
                else:
                    await dclient.send_message(msg.channel, 'You\'re currently not in a voice channel!')
                while True:
                    try:
                        if player.is_done():
                            await voice.disconnect()
                            break
                    except:
                        break

dclient.run(Token_ID)
