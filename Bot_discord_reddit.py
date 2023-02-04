#!/usr/bin/env python3

import discord 
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True

client = commands.Bot(command_prefix=',', intents=intents)

@client.event
async def on_ready():
    print("hello world")

@client.event 
async def on_message(message):
    if message.content.startswith("/upvote"):
        print(message.author.name)
        if message.author.name != "Bot_reddit":
            print(message.content)
    

client.run("MTA3MTQ0NzA3NjMwODc5NTQ4Mg.G84v67.g5QV9cHMoMc_udH9B3wjhO-q--MloE9eemcnxI")
