import discord
import asyncio
import json
import urllib.request
import random
from datetime import datetime, timedelta
from math import floor
from affix import affixes

client = discord.Client()
officersID = ['204420413814472704']


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    global officersID

    if message.content.startswith('!thelp'):
        await client.send_message(message.channel, '```Available TEST commands for this Channel:' 
            '\n!tselect - Test version of random member select.'
            '\n\tThis randomly selects a member from a pre-defined channel'
            '\n!tofficer - test version of officer only commands'
            '\n\tThis command only works for users with a certain role```'
            )

## Available to specified Roles ONLY
# 380763363908648963 - Test_Role
 
    #if '380763363908648963' in (y.id for y in message.author.roles):

        ## These are the test version commands
        # await client.send_message(message.channel, "```Officer Command Invoked```")
    if (message.content.startswith('!tofficer')) and ('380763363908648963' in (y.id for y in message.author.roles)) :
        await client.delete_message(message)
        await client.send_message(message.channel, '```Confirmed```')
        ## Test version END

    elif (message.content.startswith('!tup')) and ('380763363908648963' in (y.id for y in message.author.roles)):
        for x in officersID:
            # Moves everyone in officersID list to Officer channel 
            await client.move_member(client.get_server('336532282678575104').get_member(x), client.get_channel('336532282678575106'))
        await client.delete_message(message)

    elif (message.content.startswith('!tdown')) and ('380763363908648963' in (y.id for y in message.author.roles)) :
        for x in officersID:
            # Moves everyone in officersID list to Raid channel 
            await client.move_member(client.get_server('336532282678575104').get_member(x), client.get_channel('380762592400113665'))
        await client.delete_message(message)


## Available to all Roles :)

    elif message.content.startswith('!tselect') and ('380763363908648963' in (y.id for y in message.author.roles)):
        officersID = ['204420413814472704']
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
            #print('ran_mem: ' + str(ran_mem))  ## Debugging
            #print(members[ran_mem].id)  ## Debugging
            #if (members[ran_mem].id not in officersID):
                #print('chosen: ' + str(members[ran_mem].name)) 
                #await client.send_message(message.channel, str(members[ran_mem].name)+' has been choosen!')
                #officersID.append(str(members[ran_mem].id))
                #print(officersID)

            # This loop will be active as long as the selected person is an officer
            # it will keep getting a new random int to select a new person until the new person is
            # not in officersID. If also includes a debugging print statement
            while (members[ran_mem].id in officersID):
                print('ran_mem: ' + str(ran_mem))               ## Debugging: print the current random int
                print('chosen: ' + str(members[ran_mem].name))  ## Debugging: print who was chosen
                ran_mem = random.randint(0,len(members)-1)     # get new random int
            # Out of loop, selected member must NOT be in officerID already
            await client.send_message(message.channel, str(members[ran_mem].name) + ' had been choosen!')
            officersID.append(str(members[ran_mem].id))
            print(officersID)   ## Debugging
        # END IF

    elif message.content.startswith('!treset') and ('380763363908648963' in (y.id for y in message.author.roles)):
        officersID = ['204420413814472704']
        await client.send_message(message.channel, '```Reset Complete```')
        print(officersID)

        #for x in gen.voice_members:
            #await client.send_message(message.channel, 'Discord RealID: '+ str(x) + ' Discord Identifier: ' + str(x.id) + ' Username: ' + str(x.name))
            #print('Discord RealID: '+ str(x) + ' Discord Identifier: ' + str(x.id) + ' Username: ' + str(x.name))
            #if x.name == 'Tuggy':
                #await client.send_message(message.channel, 'Hello Tuggy :)')

#END IF

client.run('MzgwNDMyMjQ5MzgxOTc4MTIy.DO4g_Q.6Up4UAH6VNhCnSB-osdRiQVYhM0')

#END FILE

