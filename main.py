import discord
import os
from keep_alive import keep_alive

client = discord.Client()



@client.event
async def on_ready():
  print('We have logged in as {0.user} & The Bot is Online'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('$hello'):
    await message.channel.send("just tell a hello once more I will just block you !!!!!!!")
  elif message.content.startswith('$inspire'):
    await message.channel.send("What type of Inspiration you need?")
  elif message.content.startswith('$name'):
    await message.channel.send(" ... ")
  elif message.content.startswith('$Age'):
    await message.channel.send("Square root of you age..LOL")
  elif message.content.startswith('$Place'):
    await message.channel.send('I am from Russia')  
  elif message.content.startswith('$DOB'):
    await message.channel.send("15th of August 1942")
  elif message.content.startswith('$play'):  
    await message.channel.send("Just study know ! :{")
  elif message.content.startswith('$dance'):  
    await message.channel.send("I seem to be a dancer to you?")
  elif message.content.startswith('$Sorry'):
    await message.channel.send('Ok')
  elif message.content.startswith('$friend'):
    await message.channel.send('Only female friends and in search of a good Boy not like you!@')
  elif message.content.startswith('$drama'):
    await message.channel.send("We girls are pro in that don't you know that")
  elif message.content.startswith('$crush'):
    await message.channel.send("Hm")
  elif message.content.startswith('$Eligible'):
    await message.channel.send("You are not yet eligible to get love! :)")
  elif message.content.startswith('$What?:('):
    await message.channel.send('Yus you are not eligible for love!! Understood?')
  elif message.content.startswith('$Goodmorning'):
    await message.channel.send("A very Goodmorning to you")
  elif message.content.startswith('$Goodafternoon'):
    await message.channel.send("Dont wish me so much , Btw  GoodAfternoon")
  elif message.content.startswith('$Goodnight'):
    await message.channel.send("Yes!Goodnight< dont do that thing now LOL")    
  elif message.content.startswith('$like'):
    await message.channel.send("I dont :) but someday I will think off it now go!")
  



    













keep_alive()
client.run(os.getenv('TOKEN'))




