import discord
import os
import os.path
import random
import time
import datetime

from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import datetime as dt

client = discord.Client()

@client.event
async def on_ready():
    print("Ready")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    con = message.content
    aut = message.author
    ch = message.channel
    ser = message.guild.name
    t = int( time.time() )
    user_path = f'USERS/{aut}/{ser}'

    if not os.path.exists(user_path):
        os.makedirs(f'USERS/{aut}/{ser}')
        os.makedirs(f'USERS/{aut}/{ser}/multimedia')
        os.makedirs(f'USERS/{aut}/{ser}/txt')

    #text
    with open(f'USERS/{aut}/{ser}/txt/texts.txt', 'a') as f:
        f.writelines(f'\n{ch}🀇{t}🀇{con}')

    #image
    for attachment in message.attachments:
        extension = os.path.splitext(attachment.filename)[1]
        await attachment.save(os.path.join(f'USERS/{aut}/{ser}/multimedia', f'{ch}🀇{t}{extension}'))


with open('TOKEN') as file:
    token = file.read().rstrip()
client.run(token)