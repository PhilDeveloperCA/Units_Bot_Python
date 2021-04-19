import discord
import os
import requests;
import re;
from discord.ext import commands
from unit import Base_Units, Unit
from convert_message import BasicConvert, TypeConvert

client = discord.Client()

@client.event
async def on_ready():
    print('{0.user} Connected'
          .format(client))
@client.event
async def on_message(message):
    if message.author == client.user:
      return
    if message.content.startswith('$convert.show'):
      await message.channel.send(Base_Units.keys())
      return
    if message.content.startswith('#convert.getType'):
        if(re.search('^#convert.getType:[a-zA-Z]*([*|\/][a-zA-Z]*)*', message.content)):
            response = await TypeConvert(message)
            await message.channel.send(response)
        else:
            await message.channel.send('Invalid Syntax')
        return
    if message.content.startswith('#convert.'):
      if(re.search('^#convert.[a-zA-Z]*\([0-9]+\)([*|\/][a-zA-Z0-9]*\([0-9]+\))*:[a-zA-Z]*', message.content)):
         await BasicConvert(message)
      else:
          await message.channel.send('Invalid Syntax')
      #if(re.search('^convert.+[a-zA-Z]*([0,9]*):[a-zA-Z]*', message.content)):
        #await BasicConvert(message)
    #garbage Comment 

client.run(os.environ['TOKEN'])