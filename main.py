import discord
from discord.ext import commands
import os
import random
from keys import discordkey, geminikey
import google.generativeai as genai
from embeds import helpe


genai.configure(api_key=geminikey)
model = genai.GenerativeModel('gemini-pro')





intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = '-', case_insensitive = True, activity=discord.CustomActivity(name="Use '--help' for help"), status=discord.Status.online, intents=intents)
versao = ('0.0.1')



@bot.event
async def on_ready():
  print('Entramos como {0.user}' . format(bot))


def gerar_resposta(messages):
  model.generate_content(messages)




@bot.command(name="-")
async def g(ctx, *, prompt:str):
  final=model.generate_content(prompt)
  await ctx.send(final.text)


@bot.command(name="-help")
async def h(ctx):
  await ctx.send(embed=helpe)




@bot.command()
async def teste(ctx='teste'):
  await ctx.send("Testing")






bot.run(discordkey)