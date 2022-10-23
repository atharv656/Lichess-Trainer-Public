import discord
from discord.ext import commands
import pickle
import atexit
import LichessPuzzleRecommender as puzzleRec
import os
import sys

#Add your Discord bot token here
key = "YOUR_KEY_HERE"


#Load the discord bot
intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents = intents)
bot = commands.Bot(command_prefix="!", intents=intents)

#Load the discord user to lichess account map
file = open('userList.pkl', 'rb')
try:
    accountMap = pickle.load(file)
except EOFError:
    accountMap = {}
file.close()

#Save the discord user to lichess account map
@atexit.register
def save():
    file = open('userList.pkl', 'wb')
    pickle.dump(accountMap, file)
    file.close()

@bot.event
async def on_ready():
    print(f'bot has connected to Discord!')
    try:
        #If environment variable is set, send puzzles on boot
        input = os.environ['INPUT']
        await sendDailyPuzzles()
        sys.exit()

    #If environment variable is not set, KeyError is raised and we continue
    except KeyError:
        pass

@bot.event
async def on_message(message):
    #Print to console for debugging
    print(f'USER - {message.author} texted - {message.content}')
    await bot.process_commands(message)


#Add users to accountMap
@bot.command()
async def add(ctx, accountName):
    if ctx.author.id in accountMap:
        await ctx.send(f"<@{ctx.author.id}> you can only add one account! {accountMap[ctx.author.id]} is your current account")
    else:
        author = ctx.author.id
        accountMap[author] = accountName
        await ctx.channel.send("<@{}> added Lichess account: {}".format(author, accountName))

#Change existing users info in accountMap
@bot.command()
async def set(ctx, accountName):
    print(ctx.author.id)
    if ctx.author.id in accountMap:
        await ctx.channel.send(f"<@{ctx.author.id}> changed Lichess account from {accountMap[ctx.author.id]} to: {accountName}")
    else:
        await ctx.channel.send("<@{}> no prior Lichess account was found so I added a new Lichess account: {}".format(ctx.author.id, accountName))
    accountMap[ctx.author.id] = accountName

#Send puzzles to all users in accountMap
async def sendDailyPuzzles():
    for id in accountMap.keys():
        user = await bot.fetch_user(id)
        channel = await user.create_dm()
        white, black = puzzleRec.getPuzzles()
        

        await channel.send(f"Hey {user.name}, here are your puzzles for today!")
        await channel.send(f"White: {white[0]} {white[1]}")
        await channel.send(f"Black: {black[0]} {black[1]}")
        # Prints for debugging
        # print(white)
        # print(black)
        

        # Uncomment to format the puzzles as embedded links
        # whiteMessage = discord.Embed(title=f"White to play: {white[0]}", description=white)
        # blackMessage = discord.Embed(title=f"Black to play: {black[0]}", description=black)

        # await channel.send(embed=whiteMessage)
        # await channel.send(embed=blackMessage)

# Run the bot with your key
bot.run(key)
