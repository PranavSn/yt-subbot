import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from subhelpers import subDict

load_dotenv()
DISC_TOKEN=os.getenv('DISCORD_TOKEN')
LOG_PATH=os.getenv('LOGGING_FILE')
GOOGLE_KEY=os.getenv('GOOGLE_KEY')
dict = subDict("subscriptions")


intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='$', intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
#commands
@client.command()
async def add(ctx, *args):
    cid = 
    if(len(args) == 2):
        if(args[1].lower() == "false"):
            
    

client.run(DISC_TOKEN)