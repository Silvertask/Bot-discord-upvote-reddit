#!/usr/bin/env python3

import Config_bot_reddit #Import le fichier suivant 
import discord #import la biblio discord
from discord.ext import commands #Permet d'utiliser les commades de la biblio 


intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True

import requests

url = "https://www.reddit.com/api/v1/posts/top?limit=1"
response = requests.get(url)

client = commands.Bot(command_prefix=',', intents=intents)

@client.event
async def on_ready():
    print("hello world")

@client.event 
async def on_message(message):
    if message.content.startswith("/upvote"):
            if response.status_code == 200:
                data = response.json()
                post = data["data"][0]
                title = post["title"]
                subreddit = post["subreddit"]
                score = post["score"]
            print("The most upvoted post on Reddit is '{}' from r/{} with a score of {}.".format(title, subreddit, score))
    else:
            print("Request failed with status code: {}".format(response.status_code))
    
    if message.author.name != "Bot_reddit":
            print(message.content)
    

client.run(Config_bot_reddit.Token_discord)
