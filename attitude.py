import discord
import asyncio
import json
import urllib.request
from datetime import datetime, timedelta
from math import floor
from affix import affixes

client = discord.Client()
officersID = []


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):

    if message.content.startswith('!commands'):
        await client.send_message(message.channel, '```Available commands for this Channel:' 
            '\n!logs - Guild Warcraft Logs page' 
            '\n!affix - List of Affixes for this week and next week'
            '\n!addons - Required/Suggested addons for raiding'
            '\n!invasion - Displays time until end of current invasion, or until start of next invasion```'
            )

## Available in Lads Channel
# This should be cleaned up some
    if message.channel.name == 'lads':
        if message.content.startswith('!up'):
            for x in officersID:
                # Moves everyone in officersID list to Officer channel 
                await client.move_member(client.get_server('').get_member(x), client.get_channel(''))
            await client.delete_message(message)

        elif message.content.startswith('!down'):
            for x in officersID:
                # Moves everyone in officersID list to Officer channel 
                await client.move_member(client.get_server('').get_member(x), client.get_channel(''))
            await client.delete_message(message)


## Available in General Channel

    # List guild warcraft log page, and latest log
    elif message.content.startswith('!logs'):
        logs = urllib.request.urlopen('https://www.warcraftlogs.com/v1/reports/guild/Attitude/Arthas/us?api_key=83cd4d911aecbd720692c99e4eda5e35')
        ljdata = json.load(logs)
        await client.send_message(message.channel, 'Guild Page: https://www.warcraftlogs.com/guilds/214323\nLatest Log: https://www.warcraftlogs.com/reports/' + str(ljdata[len(ljdata) - 1]['id']))

    # Lists current week affixes, as well as next week's affixes
    elif message.content.startswith('!affix'):
        d1 = datetime(2017, 3, 28)
        d2 = datetime.today()

        tuesday1 = (d1 - timedelta(days=d1.weekday()-1))
        tuesday2 = (d2 - timedelta(days=d2.weekday()))


        currentAffix = affixes[floor(((tuesday2 - tuesday1).days / 7) % 12)]
        nextAffix = affixes[floor(((tuesday2 - tuesday1).days / 7) % 12) + 1]

        output = 'This weeks affixes are: {}, {}, {}\nNext weeks affixes are: {}, {}, {}'.format(currentAffix[0], currentAffix[1], currentAffix[2],nextAffix[0], nextAffix[1], nextAffix[2])

        await client.send_message(message.channel, output)

    # Lists required addons for raiding
    elif message.content.startswith('!addon'):
        await client.send_message(message.channel, '\nRequired Addons:'
            '\nBossMod of some kind:'
            '\n\t\tDBM: <https://mods.curse.com/addons/wow/deadly-boss-mods>\n\t\tBigWigs: <https://mods.curse.com/addons/wow/big-wigs>'
            '\nWeakAuras: <https://mods.curse.com/addons/wow/weakauras-2>'
            '\nRCLootCouncil: <https://mods.curse.com/addons/wow/rclootcouncil>')

    # Shows current invasion status, and time until end or next invasion
    elif message.content.startswith('!invasion'):
        #start = Mon july 10 2017 @ 7.30pm EST
        start = datetime(2017, 7, 10, 18, 30)

        now = datetime.now()
        loop = True
        enabled = True

        # Check to see if an invasion is up or not
        while loop:
            if enabled:
                start = start + timedelta(hours=6)
                if now < start: # Exits loop, invasion is happening
                    loop = False
                    nexttime = start - now
                    await client.send_message(message.channel,"There is an invasion active now!\nTime left: " + str(nexttime).split('.',2)[0])
                else:
                    enabled = False
            else:
                start = start + timedelta(hours=12, minutes=30)
                if now < start: # Exits loop, invasion not happening
                    loop = False
                    nexttime = start-now
                    await client.send_message(message.channel,"There is no invasion active.\nTime until next invasion: " + str(nexttime).split('.',2)[0])
                    
                else:
                    enabled = True


#END IF

client.run('MzMyNjg1MzA2MDQwMDI1MTEw.DEUqXw.6Sdm3v1a0QK535FLlm3yCOwDxFM')

#END FILE
