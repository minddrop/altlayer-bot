import discord
import random
from discord.ext import commands

client = discord.Client()
bot = commands.Bot(command_prefix='!')


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


client.run(ALTLAYER_BOT_TOKEN)
