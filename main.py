import os
import discord
from dotenv import load_dotenv

load_dotenv(dotenv_path="config")
load_dotenv(dotenv_path="Clef")

TOKEN = os.getenv("TOKEN")
client = discord.Client()

@client.event
async def on_ready():
    print("Sstem ON")



client.run(TOKEN)
