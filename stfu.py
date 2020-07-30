import discord
import random
from discord.ext import commands ,tasks
from discord.utils import get
import os
import time
import asyncio

client = commands.Bot(command_prefix = "egg ")

token = "NzM3NjM5ODk0MTIxNDQ3NDU0.XyASrw.vF6Sav7VRxcsR926pjH5dunHoxI"

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Search The EGG'))
    print('ON !')

@client.command()
async def guess(ctx,message):
    if message.lower() == "storage-website-gacha.herokuapp.com/egg.html":
        await ctx.author.send(embed=discord.Embed(title="You got one thing"))
    elif message.lower() == "stfurequiemisthebestbot":
        embed = discord.Embed()
        embed.set_image(url='http://storage-website-gacha.herokuapp.com/Image/enigma.png')
        await ctx.author.send(embed=embed)
    elif message.lower() == "stfuplease!":
        await ctx.author.send(embed=discord.Embed(title="Search in summons you shall find the answer"))
    elif message.lower() == "stfuplease!":
        await ctx.author.send(embed=discord.Embed(title="https://discord.gg/HGnPJH4"))
    else:
        await ctx.author.send(embed=discord.Embed(title="Try agin !"))
    await ctx.message.delete()


@client.command()
async def hint(ctx):
    embed = discord.Embed(title='The first answer Is were you started')

    await ctx.author.send(embed=embed)


client.run(token)