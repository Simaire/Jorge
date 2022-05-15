import os
import discord
from dotenv import load_dotenv
import openai

load_dotenv(dotenv_path="config")
load_dotenv(dotenv_path="Clef")

TOKEN = os.getenv("TOKEN")
openaikey = os.getenv("openaikey")

client = discord.Client()

@client.event
async def on_ready():
    print("Sstem ON")

@client.event
async def on_message(message):

    Bot = message.author.bot

    print("Msg Recue")
    if Bot == False:
        print("Par un human")

        openai.api_key = openaikey

        start_sequence = "\n "
        restart_sequence = "\nHuman: "

        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt="Ce qui suit est une conversation avec un assistant IA. L'assistant est serviable, créatif, intelligent et très sympathique. Il s'apelle Jorge\n\nHumain : Bonjour, qui êtes-vous ?\n Je suis une IA créée par OpenAI. Comment puis-je vous aider aujourd'hui?\nHuman: " + message.content,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"]
    )
        content = response.choices[0].text


        await message.channel.send(content)

    if Bot == True:
        print("Par un robot")

    if Bot != True and Bot != False:
        print("Eror")

client.run(TOKEN)
