discordbot
=============

A fairly simple discord bot written in python.

* I've started an implementation of .mp3 playback within the bot, so please note it's not the greatest nor the most reliable.

This software uses libraries from the FFmpeg project under the LGPLv2.1

### Windows Installation

1) Download latest Python version 3.5+: https://www.python.org/downloads/windows/, then open the .exe file to start the installation.

2) Open up Command Prompt with Administrative privileges.
Click on start menu and type 'cmd' and then right click on the Command Prompt and click run as Administrator. (Administrator mode is needed in order to run installations through Python.)

3) Run the command in Command Prompt to install the Discord Python API:
```PowerShell
python -m pip install asyncio discord.py
```

4) Download the bot files from Github and store them where you'd like

5) Edit config.ini with your bot information

6) When you're done configuring, open bot.py and if all's well, you should have no errors.