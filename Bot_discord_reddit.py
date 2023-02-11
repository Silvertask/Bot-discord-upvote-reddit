#!/usr/bin/env python3

import Config_bot_reddit #Import le fichier suivant 
import discord #import la biblio discord
from discord.ext import commands #Permet d'utiliser les commandes de la biblio 


intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True

import requests

url = "https://api.reddit.com/r/all/top?limit=1&t=day"
response = requests.get(url)

client = commands.Bot(command_prefix=',', intents=intents)

@client.event
async def on_ready():
    print("hello world")

@client.event 
async def on_message(message):


    if message.content.startswith('/upvote'):
        response = requests.get("https://api.reddit.com/r/all/top?limit=1&t=day")
        data = response.json()
        title = data["data"]["children"][0]["data"]["title"]
        votes = data["data"]["children"][0]["data"]["ups"]
        link = data["data"]["children"][0]["data"]["url"]
        msg = f"Post le plus upvote dans les dernières 24 heures: {title} ({votes} votes) - {link}"
        await message.channel.send(msg)
    
    if message.author.name != "Bot_reddit":
            print(message.content)
    

client.run(Config_bot_reddit.Token_discord)
