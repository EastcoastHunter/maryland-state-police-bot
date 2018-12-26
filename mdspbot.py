import discord
import asyncio
import Pymoe
import simplejson as json
import request as rq
from champs import champs 
import random
import pickle
import os









api = str(os.envion.get('RIOT_KEY'))








An=Pymoe.Anilisst()

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('/test'):
        counter = 10
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 10

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('/sleep'):
        await asyncio.sleep(20)
        await client.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith('/flip'):
        flip = random.choice(['Heads','Tails'])
        await client.send_message(message.channel, flip)
    elif message.content.startswith('/addquote'):
        if not os.path.isfile("quote_file.pk1"):
            quote_list = []
        else:
            with open("quote_file.pk1", "rb") as quote_file:
                quote_list = pickle.load(quote_file)
        quote_list.append(message.content[9:])
        with open("quote_file.pk1" , "wb") as quote_file:
            pickle.dump(quote_list , quote_file)
    elif message.content.startswith('/quote'):
        with open("quote_file.pk1", "rb") as quote_file:
            quote_list = pickle.load(quote_file)
        await client.send_message(message.channel, random.choice(quote_list))
    elif message.content.startswith('/hooters'):
        await client.send_message(message.channel, 'If you want to get some hooters go to your local hooters resturant')
    elif message.content.startswith('/meme'):
        await client.send_message(message.channel, 'Your face is a meme so stop using this command')
    elif message.content.startswith('/help'):
        await client.send_message(message.channel, ' commands are as followed `/test`, `/sleep`, `/addquote`,`/quote`,`/hooters`,`/meme`,`/help: which shows this message`')
       
client.login(process.env.BOT_TOKEN)
