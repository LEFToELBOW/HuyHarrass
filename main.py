import discord
import os
from discord.utils import get
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready(): 
  print("bot ready")
  

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith("<:wassupcuties:873411655122444310>") or message.content.startswith("<:permaster:867448195117350953>") or message.content.startswith("<:huy:907010727158632528>") or message.content.startswith("<:cutefucker:916110012173123634>") or message.content.startswith("🐷") or message.content.startswith("🤡"):
    await message.channel.send(f"<@{366353178641301506}>")
  

keep_alive()

client.run(os.getenv("TOKEN"))
