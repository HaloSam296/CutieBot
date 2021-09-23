import discord
from discord.ext import commands
from discord.utils import get
import os
import random
from StayinAlive import keepAlive

Token = os.environ['Token']
description = "A small cute bot mostly built by AGrapplerNamedSam. VERY, VERY WIP"
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)


@bot.event
async def on_ready():
  print('Logged in as')
  print(bot.user.name)
  print("Bot ID: " + str(bot.user.id))
  print('------')


@bot.command(pass_context=True)
async def confirm(ctx):
  role = get(ctx.author.guild.roles, name = 'n00b')
  await ctx.author. add_roles(role, ctx.author)


bot.remove_command("help")
@bot.group(invoke_without_command=True)
async def help(ctx):
  Emb = discord.Embed(title='Help',description='The Help Menu. Ask AGrapplerNamedSam or a mod for more help.')
  Emb.add_field(name='?roll [NdN]', value='Rolls a set of dice.', inline = True)
  Emb.add_field(name='?choose [arg1, arg2, ...]', value='Randomly chooses between a set of options.', inline =True)
  Emb.add_field(name='?coinflip', value='Do I really need to explain this one?', inline = True)
  Emb.add_field(name='?joined [@user#0000]', value='Displays when a user has joined the server.', inline = True)
  Emb.set_footer(text='More commands can be added upon request!')

  await ctx.send(embed = Emb)


@bot.command()
async def roll(ctx, dice: str):
  """?roll [NdN]-Rolls a set of dice."""
  dice = dice.lower()
  RollNumber, DieNumber = int(dice[0]), int(dice[2:])
  AddedNumber = 0
  Result = 'Result: '

  for i in range(RollNumber):
    roll = random.randint(1, DieNumber)
    AddedNumber = AddedNumber+int(roll)
    rollString = str(roll)
    Result = Result+' '+rollString

  await ctx.send(Result+" = " +str(AddedNumber))


@bot.command()
async def choose(ctx, *choices: str):
  """?choose [arg1, arg2,...]-Randomly chooses between a set of options."""
  await ctx.send(random.choice(choices))


@bot.command()
async def coinflip(ctx):
  """?coinflip-Do I really need to explain this one?"""
  Coin = ["Heads", "Tails"]
  await ctx.send(random.choice(Coin))


@bot.command()
async def joined(ctx, member: discord.Member):
  """?joined [@user#0000]-Displays when a user has joined the server."""
  await ctx.send('{0.name} joined in {0.joined_at}'.format(member))


keepAlive()
bot.run(Token)