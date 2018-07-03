import discord
import random
import os
from discord.ext import commands

client = discord.Client()
bot = commands.Bot(command_prefix='!')
token = os.getenv('ALTLAYER_BOT_TOKEN')


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content == '!ping':
        if client.user != message.author:
            await client.send_message(message.channel, 'pong')
    if message.content == '!dice':
        if client.user != message.author:
            r = random.randint(0, 4)
            member = ['minddrop', 'kyasbal', 'moajo', 'pnly', 'akatukigyou']
            await client.send_message(message.channel, member[r])


client.run(token)
