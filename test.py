############################
# TEST VERSION
############################

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

    roles = []

    print(message.author.roles)

    for role in message.author.roles:
        roles.append(role.name)

    print(roles)
    if 'Test_Role' in roles:
        print('yup, its there')

    if message.author == client.user:
        return

    if message.content.startswith(prefix):
        print(message.content)                  # print our initial command string
        terms = message.content[1:].split()     # strips the leading ! and splits the command string
        command = terms[0].lower()              # pulls the first term, aka the command, and casts to lower
        print(command)                          # verify we have the first term by printing it
        if len(terms) > 1:
            for x in terms[1:]:
                print(x)                        # print the next terms
        

client.run('MzgwNDMyMjQ5MzgxOTc4MTIy.DUc9dQ.WU-NbNx6M-GN0xOhsx4bdryRUBg')

#END FILE

