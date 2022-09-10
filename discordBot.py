import discord
from discord.ext import commands
import pickle
import atexit
import LichessPuzzleRecommender as puzzleRec
import os
import sys

intents = discord.Intents.default()
intents.members = True

client = discord.Client()
bot = commands.Bot(command_prefix="!", intents=intents)

file = open('userList.pkl', 'rb')
try:
    accountMap = pickle.load(file)
except EOFError:
    accountMap = {}
file.close()

@atexit.register
def save():
    file = open('userList.pkl', 'wb')
    pickle.dump(accountMap, file)
    file.close()

@bot.event
async def on_ready():
    print(f'bot has connected to Discord!')
    try:
        input = os.environ['INPUT']
        await sendDailyPuzzles()
        sys.exit()

    except KeyError:
        pass

@bot.event
async def on_message(message):
    print(f'USER - {message.author} texted - {message.content}')
    await bot.process_commands(message)


@bot.command()
async def add(ctx, accountName):
    if ctx.author.id in accountMap:
        await ctx.send(f"<@{ctx.author.id}> you can only add one account! {accountMap[ctx.author.id]} is your current account")
    else:
        author = ctx.author.id
        accountMap[author] = accountName
        await ctx.channel.send("<@{}> added Lichess account: {}".format(author, accountName))

@bot.command()
async def set(ctx, accountName):
    print(ctx.author.id)
    if ctx.author.id in accountMap:
        await ctx.channel.send(f"<@{ctx.author.id}> changed Lichess account from {accountMap[ctx.author.id]} to: {accountName}")
    else:
        await ctx.channel.send("<@{}> no prior Lichess account was found so I added a new Lichess account: {}".format(ctx.author.id, accountName))
    accountMap[ctx.author.id] = accountName

async def sendDailyPuzzles():
    for id in accountMap.keys():
        user = await bot.fetch_user(id)
        channel = await user.create_dm()
        white, black = puzzleRec.getPuzzles()
        whiteMessage = discord.Embed(title=f"White to play: {white[0]}", description=white)
        blackMessage = discord.Embed(title=f"Black to play: {black[0]}", description=black)
        
        await channel.send(f"Hey {user.name}, here are your puzzles for today!")
        await channel.send(embed=whiteMessage)
        await channel.send(embed=blackMessage)

def test():
    print("test")


bot.run("OTI0NDcyNjkyODY0ODQ3OTEz.YcfESQ.g1sUsdsz20IUehvQ-qgAQ9RpsIE")
