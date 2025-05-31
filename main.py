import discord
from discord.ext import commands
import os
import random
from keys import discordkey, geminikey
import google.generativeai as genai
from embeds import helpe


genai.configure(api_key=geminikey)
model = genai.GenerativeModel('gemini-2.0-flash')


## Bot Connection ##


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = '-', case_insensitive = True, activity=discord.CustomActivity(name="Use '--help' for help"), status=discord.Status.online, intents=intents)
versao = ('0.0.1')


@bot.event
async def on_ready():
  print('Entramos como {0.user}' . format(bot))




## Gemini Commands ##



def gerar_resposta(messages):
  model.generate_content(messages)




@bot.command(name="-")
async def g(ctx, *, prompt:str):
  final=model.generate_content(f'{prompt}.Follow the language of the message.', generation_config=genai.types.GenerationConfig(max_output_tokens=500))
  await ctx.send(final.text)



## General Commands ##

@bot.command(name="-help")
async def h(ctx):
  await ctx.send(embed=helpe)




@bot.command()
async def teste(ctx='teste'):
  await ctx.send("Testing")

@bot.command()
async def ping(ctx='ping'):
  await ctx.send("pong!")





if __name__ == "__main__":
  bot.run(discordkey)