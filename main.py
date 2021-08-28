import discord
import os
import requests
import json
import random
from replit import db


client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "dissapointed"]
bad_words = ["tangina","bobo","putangina","pakyu","gago","bitch","fuck","puta"]
sana_ll = ["sana all", "sanaol", "naol"]

naol_words = ["mapapa sana ol ka na lang talaga :upside_down: "]

bawal_yan = [
  "Pasmado naman ng bibig mo!:face_with_symbols_over_mouth: ",
  "Bad word yan lods :grimacing: ",
  "Ano ba yan pala mura :woozy_face: ",
  "Kailangan mag mura lods?:thinking:  "
]
starter_encouragements = [
  "Cheer up! -RoboG :hearts: ",
  "You got this! -RoboG :innocent: ",
  "You are a great person. -RoboG :innocent: ",
  "Calm down and take some rest. -RoboG :innocent: ",
  "Everything will be fine. :relieved: "
]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client:
    return

  if message.content.startswith('\hello'):
    await message.channel.send('Hello!')

  if message.content.startswith('\hi'):
    await message.channel.send('Hi!')

  msg = message.content

  if message.content.startswith('\Quote'):
    quote = get_quote()
    await message.channel.send(quote)

  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encouragements))
  
  if any(word in msg for word in bad_words):
    await message.channel.send(random.choice(bawal_yan))

  if any(word in msg for word in sana_ll):
    await message.channel.send(random.choice(naol_words))


client.run(os.environ['EDOC'])