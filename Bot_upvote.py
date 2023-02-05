#!/usr/bin/env python3

import discord
from discord.ext import commands
import praw

client = commands.Bot(command_prefix='/')

@client.command()
async def upvote(ctx):
    reddit = praw.Reddit(client_id='YOUR_CLIENT_ID', client_secret='YOUR_CLIENT_SECRET', username='YOUR_USERNAME', password='YOUR_PASSWORD', user_agent='YOUR_USER_AGENT')
    top_post = reddit.subreddit('all').hot(limit=1)
    for post in top_post:
        await ctx.send(post.title)
        await ctx.send(post.url)

client.run('YOUR_DISCORD_TOKEN')
