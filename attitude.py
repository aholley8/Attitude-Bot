

import discord
import asyncio
import json
import urllib.request
import random
from datetime import datetime, timedelta
from math import floor
from affix import affixes
from dict import DictionaryReader


client = discord.Client()

officersID = [
    '204420413814472704', #Alex
    '229757511715127296', #Sammy
    '218079956888977409', #Bruise
]

#'90170201890394112',  #Nate
#'216036936433795084', #Caleb
#'187392035890659328', #Gummy
#'229981371928412160', #Kyo

## IDs for Attitude
server_id = '245634401046626304' 
## Voice Channels
lads_voice = '396058528600817674'
raid_voice = '246053446287884298'
## Roles
officer_role = '245636355311403008'
## Text Channel
lads_text = '396058468479664138'

prefix = '!'

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    global officersID

    # Ignore and messages made by the bot
    if message.author == client.user:
        return

    # Ignore any message that does not have the prefix
    if not message.content.startswith(prefix):
        return

    d = DictionaryReader()

    # This list will contain the author's roles to check against later, only works in a server (ie not with PMs)
    try:
        roles = []
        for role in message.author.roles:
            roles.append(role.name)

        print(roles)
    except:
        pass


# ----------------------------------------------------------------------------------------
## Available to Officers Only
# ----------------------------------------------------------------------------------------

    if (message.content.startswith(prefix+'officer')) and ('Officers' in roles): 
        await client.send_message(client.get_channel(lads_text), '```Available commands for Officers:' 
            '\n!up - moves Loot Council up to Officer chat' 
            '\n!down - moves Loot Coucil back down to Raid Chat'
            '\n!select - selects a member from current voice channel and adds them to Loot Council'
            '\n!reset - Clears and resets Loot Council.```'
            )

# Lads text channel
# '245637944453365761'

    if (message.content.startswith(prefix+'up')) and ('Officers' in roles): 
        print(officersID)
        for x in officersID:
            #print(officersID)
            # Moves everyone in officersID list to Officer channel 
            await client.move_member(client.get_server(server_id).get_member(x), client.get_channel(lads_voice))
        await client.delete_message(message)

    if (message.content.startswith(prefix+'down')) and ('Officers' in roles) :
        for x in officersID:
            # Moves everyone in officersID list to Raid channel 
            await client.move_member(client.get_server(server_id).get_member(x), client.get_channel(raid_voice))
        await client.delete_message(message)


 
    if message.content.startswith(prefix + 'select') and ('Officers' in roles):
        officersID = ['204420413814472704','229757511715127296','218079956888977409']
        print('officersID before select:')
        print(officersID)
        #await client.send_message(message.channel, message.author.id)  ## Debugging
        #members = client.get_channel('336532282678575106').voice_members  
        members = message.author.voice.voice_channel.voice_members
        # returns a list of members in the specified channel
        print('Length of members list: ' + str(len(members)))  ## Debugging
        # Check to see if there are users before trying to select one
        if (len(members) > 0):
            ran_mem = random.randint(0,len(members)-1)
            # This loop will be active as long as the selected person is an officer
            # it will keep getting a new random int to select a new person until the new person is
            # not in officersID. If also includes a debugging print statement
            while (members[ran_mem].id in officersID):
                print('ran_mem: ' + str(ran_mem))               ## Debugging: print the current random int
                print('chosen: ' + str(members[ran_mem].name))  ## Debugging: print who was chosen
                ran_mem = random.randint(0,len(members)-1)     # get new random int
            # Out of loop, selected member must NOT be in officerID already
            print(str(members[ran_mem].nick))
            await client.send_message(message.channel, str(members[ran_mem].name) + ' has been choosen!')
            officersID.append(str(members[ran_mem].id))
            print(officersID)   ## Debugging
        # END IF

    if message.content.startswith(prefix + 'reset') and ('Officers' in roles):
        officersID = ['204420413814472704','229757511715127296','218079956888977409']
        print('LC reset')
        await client.delete_message(message)

# ----------------------------------------------------------------------------------------
## Available to everyone else
# ----------------------------------------------------------------------------------------

    # List guild warcraft log page, and latest log
    if message.content.startswith(prefix + 'logs'):
        logs = urllib.request.urlopen('https://www.warcraftlogs.com:443/v1/reports/guild/Lads/Illidan/us?api_key=dda5ca9f0cfe5a832b869a5b193271d1')
        ljdata = json.load(logs)
        await client.send_message(message.channel, 'Guild Page: https://www.warcraftlogs.com/guilds/339520\nLatest Log: https://www.warcraftlogs.com/reports/' + str(ljdata[len(ljdata) - 1]['id']))
    
    # Lists current week affixes, as well as next week's affixes
    if message.content.startswith(prefix + 'affix'):
        d1 = datetime(2017, 3, 28)
        d2 = datetime.now()
        
        currentAffix = affixes[floor(((d2 - d1).days / 7) % 12)]
        nextAffix = affixes[floor((((d2 - d1).days / 7) + 1) % 12)]

        output = 'This weeks affixes are: {}, {}, {}\nNext weeks affixes are: {}, {}, {}'.format(currentAffix[0], currentAffix[1], currentAffix[2],nextAffix[0], nextAffix[1], nextAffix[2])
        await client.send_message(message.channel, output)


    # Shows current invasion status, and time until end or next invasion
    if message.content.startswith(prefix + 'invasion'):
        #start = Mon july 10 2017 @ 6.30pm CST
        start = datetime(2017, 7, 10, 18, 30)

        # remove the timedelta when DST is over :P
        now = datetime.now()+timedelta(hours=1)
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

    if message.content.startswith(prefix):
        print(message.content)
        terms = message.content[1:].split()
        command = terms[0].lower()
        msg = d.readDict(command)
        # this should check if the string is empty or not.
        if msg:   
            await client.send_message(message.channel,msg)

#END IF

file = open("token.json",'r')
tokenObj = json.load(file)
file.close()
client.run(tokenObj['token'])

#END FILE

