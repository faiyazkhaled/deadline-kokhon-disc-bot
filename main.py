import discord
from discord.ext import commands
#import random
import os
import requests
import json
#features:
#Can add deadlines
#can tell jokes
#can reply to some texts[will add it more]

#can delete msgs[koita message delete kora jaabe oita bolte parbo{everyone can do}]
#[future] can generate links
#[future]can give push notifications
 
#from replit import db

client = commands.Bot(command_prefix = '.')
admin_list = ["Faiyaz Bin Khaled#8216"]
#client = discord.Client()

async def on_member_join(member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Welcome {member.mention} to {guild.name}!\nDeadline er pera er jonne ready hon'
            await guild.system_channel.send(to_send)

def get_jokes():
  response = requests.get('https://official-joke-api.appspot.com/jokes/random')
  json_data = json.loads(response.text)
  joke = json_data['setup']+ " -"+ json_data['punchline']+"\nBA DUM TSS!"+ "\nJoke tah osthir chilona bhai? Aro bhalo joke chaile mirror er dike takan"
  return(joke)

@client.event
async def on_ready():
  print("Apnar jatra shuru holo, {0.user}".format(client))


deadlines = {}
@client.event
async def on_message(message, amount = 5):
  if message.author==client.user:
    return

  if message.content.startswith("$dlAseNaki"):
    await message.channel.send("Ase maybe, eta toh BRAC :( ")
  
  if message.content.startswith("$jokebolen"):
    joke = get_jokes()
    await message.channel.send(joke)

  if(message.content.startswith("$add")):
    d = message.content[5:]
    deadline = d.split(" ")
    deadlineSub =  deadline[0]
    deadlineDate = deadline[1]
    #deadlineeee = deadlineDate +" "+ deadlineSub 
    deadlines[deadlineSub] = deadlineDate
    #await message.channel.send(deadlineeee)  
  
  if(message.content.startswith("$show")):
    for i in deadlines:
      k = i
      l = deadlines[i]
      res = k + " " + l
      
      await message.channel.send(res)
  if message.content.startswith("$del"):
    await message.channel.purge(limit = amount)


@client.command(pass_context = True)

async def clear(ctx, amount = 5):
  await ctx.channel.purge(limit = amount)

@client.command(pass_context = True)
async def foo(ctx, arg):
    await ctx.send(arg)

@client.command(pass_context=True)
async def purge(ctx, amount=5):
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=amount + 1):
              messages.append(message)

    await channel.delete_messages(messages)
    await ctx.send(f'{amount} messages have been purged by {ctx.message.author.mention}')


client.run(os.getenv('TOKEN'))

  
