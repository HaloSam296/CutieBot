import discord
from discord.ext import commands, tasks
from discord.utils import get
import random
import asyncio


description = "A small cute bot built by AGrapplerNamedSam."
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='?', description=description, intents=intents, case_insensitive=True)


def setup(bot):
	bot.add_command(confirm)
	bot.add_command(filth)
	bot.add_command(filthy)
	bot.add_command(roll)
	bot.add_command(choose)
	bot.add_command(coinflip)
	bot.add_command(joined)
	bot.add_command(joinedall)


@commands.command(pass_context=True)
async def confirm(ctx):
	role = get(ctx.author.guild.roles, id = 644946587000504335)
	print(role)
	f = open('logs/newlyjoined.txt','a')
	f.write(str(ctx.author)+" has joined ET.")
	f.close
	await ctx.author.add_roles(role, ctx.author)
	print(str(ctx.author)+" has been given the n00b role.\n")

  
@commands.command(aliases=['f'])
async def filth(ctx, idiot):
	await ctx.send("To hell with you, " + str(idiot) +" for that post you inferior twat. \nhttps://youtu.be/o048xeNQ3Wo") 


@commands.command(aliases=['fy'])
async def filthy(ctx):
	await ctx.send("To hell with you for that post, you inferior twat. \nhttps://youtu.be/o048xeNQ3Wo")


@commands.command(aliases=["r"])
async def roll(ctx, dice: str):
	dice = dice.lower()
	RollNumber, DieNumber = int(dice[0]), int(dice[2:])
	AddedNumber = 0
	Result = 'Result: '
	for i in range(RollNumber):
		roll = random.randint(1, DieNumber)
		AddedNumber = AddedNumber+roll
		rollString = str(roll)
		Result = Result+' '+rollString
	await ctx.send(Result+" = " +str(AddedNumber)+'.')


@commands.command()
async def choose(ctx, *choices: str):
	print(choices)
	await ctx.send(random.choice(choices))


@commands.command(aliases=["cf"])
async def coinflip(ctx):
	Coin = ["Heads", "Tails"]
	await ctx.send(random.choice(Coin))


@commands.command()
async def joined(ctx, member: discord.Member):
	if member.id == 315565100226576394:
		await ctx.send("AGrapplerNamedSam joined in 2019-11-29 04:20:20.393000")
	else:
		await ctx.send('{0.name} joined in {0.joined_at}'.format(member))


@commands.command(aliases=['ja'])
async def joinedall(ctx):
	for member in ctx.guild.members:
		await ctx.send('{0.name} joined in {0.joined_at}'.format(member))