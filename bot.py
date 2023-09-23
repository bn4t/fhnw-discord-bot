import string

import discord
import os # default module
from dotenv import load_dotenv
from gpt4all import GPT4All

load_dotenv() # load all the variables from the env file
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name="llm-info", description= "Get info about the llm bot")
async def info(ctx):
    await ctx.respond("I am running "+os.getenv("MODEL_NAME"))

@bot.slash_command(name = "ask", description = "Ask the LLM something")
async def ask(ctx: discord.ApplicationContext, prompt: str):
    prompt = ("You are an AI model designed to answer questions accurately. Continue directly with an answer for the following question: ")+prompt
    print(prompt)
    await ctx.defer()

    await ctx.respond(model.generate(prompt, max_tokens=150))


if __name__ == '__main__':
    model = GPT4All(os.getenv("MODEL_NAME"))
    bot.run(os.getenv('TOKEN')) # run the bot with the token