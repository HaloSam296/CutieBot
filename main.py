import discord
from discord.ext import commands
from discord.utils import get
import os
import random
import asyncio
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
	await ctx.author.add_roles(role, ctx.author)


#THIS IS COMMENTED OUT, THIS WILL NOT RUN EVEN IF A USER CALLS THE COMMAND (RUNS THE COMMAND)
'''@bot.command()
async def beannoying(ctx):
  await ctx.send('@everyone')
'''


#EASTER EGGS BELOW, PLEASE DO NOT READ
#IF YOU ARE EXAMINING HOW THE BOT WORKS,
#READ THE LAST THREE LINES AND NOTHING
#ELSE. THE LAST THREE SHOW THE EXAMPLE 
#EGG AND THE COMMAND THAT ALLOWS COMMANDS
#TO KEEP WORKING
#
# Start of the easter eggs
@bot.event
async def on_message(message):
	if message.author == bot.user:
		return
	message.content = message.content.lower()
	if "sophie" in message.content:
		await message.channel.send("Wow, that Sophie person sounds like such a cutie!")
#	if "samko" in message.content:
#		await message.channel.send("You mean Smako/Smegma?")
#	if "69" in message.content:
#		await message.channel.send("Nice.")
	if "dan" in message.content:
		await message.channel.send("What a chad!")
#	if "john" in message.content:
#		await message.channel.send("By John do you mean i-granddaddy?")
	if "halo reach" in message.content:
		await message.channel.send("I wasn't paying attention, did someone mention the best Halo?")
	
	
	if "example123456" in message.content:
		await message.channel.send("Example easter egg!")
	await bot.process_commands(message)
#
#
#
#
# End of the easter eggs



bot.Toggle = True
bot.x = 0
@bot.command(aliases=["tb"])
@commands.has_role("Warden")
async def togglebonk(ctx):
	bot.x = bot.x+1
	if bot.x % 2 == 0:
		bot.Toggle = True
		print("Bonk toggle on by", str(ctx.author))
		await ctx.send("Bonk commands toggled on.")
	elif bot.x % 2 == 1:
		bot.Toggle = False
		print("Bonk toggle off by", str(ctx.author))
		await ctx.send("Bonk commands toggled off.")
	else:
		await ctx.send("Uhhhhh... @AGrapplerNamedSam#5801... a bug happened in togglebonk()")
	return bot.x, bot.Toggle


@bot.command(aliases=["bs"])
async def bonksetting(ctx):
	if bot.Toggle == True:
		await ctx.send("Bonk commands are turned on.")
	elif bot.Toggle == False:
		await ctx.send("Bonk commands are turned off.")
	else:
		await ctx.send("ERROR @AGrapplerNamedSam#5801, bonksetting has failed. Somehow")


@bot.command(aliases=["fb"])
async def fullbonk(ctx, samkox: discord.Member):
	if bot.Toggle == True:
		BonkChannel = discord.utils.get(ctx.guild.channels, name = "JoJo's Jail")
		if samkox.voice.self_stream:
			await ctx.send(str(samkox) +" is streaming and cannot be bonked.")
			return
		elif samkox.voice.self_video:
			await ctx.send(str(samkox) +" is streaming and cannot be bonked.")
		else:
			await samkox.move_to(BonkChannel)
	elif bot.Toggle == False:
		await ctx.send("Bonk commands are disabled")
	else:
		await ctx.send("Uhhhhh... @AGrapplerNamedSam#5801... a bug happened in fullbonk()")
  


@bot.command(aliases=["qb"])
async def quickbonk(ctx, samkox: discord.Member):
	if bot.Toggle == True:
		OriginalChannel = samkox.voice.channel
		BonkChannel = discord.utils.get(ctx.guild.channels, name = "JoJo's Jail")
		if samkox.voice.self_stream:
			await ctx.send(str(samkox) +" is streaming and connot be bonked.")
		elif samkox.voice.self_video:
			await ctx.send(str(samkox) +" is streaming and cannot be bonked.")
		else:
			await samkox.move_to(BonkChannel)
		await asyncio.sleep(3.5)
		await samkox.move_to(OriginalChannel)
	elif bot.Toggle == False:
		await ctx.send("Bonk commands are disabled")
	else:
		await ctx.send("Uhhhhh... @AGrapplerNamedSam#5801... a bug happened in quickbonk()")


bot.remove_command("help")
@bot.group(invoke_without_command=True)
async def help(ctx):
	Emb = discord.Embed(title='Help',description='The Help Menu. Ask AGrapplerNamedSam or a mod for more help.')
	Emb.add_field(name='?roll [NdN]', value='Rolls a set of dice.', inline = True)
	Emb.add_field(name='?choose [arg1, arg2, ...]', value='Randomly chooses between a set of options.', inline =True)
	Emb.add_field(name='?coinflip', value='Do I really need to explain this one?', inline = True)
	Emb.add_field(name='?joined [@user#0000]', value='Displays when a user has joined the server.', inline = True)
	Emb.add_field(name='?fullbonk [@example]', value='(fb) Bonk a bad boi and send them to jail! [toggled on/off]', inline=True)
	Emb.add_field(name='?quickbonk [@example]', value='(qb) Bonk a bad boi and send them to jail for five seconds! [Toggled on/off]')
	Emb.add_field(name='?joinedall', value="Lists when every member (bots included) joined the server. Exports a LOT of text, do NOT use to spam and do NOT use outside #bot-spam!")
	Emb.add_field(name="?bonksetting", value="Outputs whether bonk commands are on or off.")
	Emb.set_footer(text='More commands can be added upon request!')
	await ctx.send(embed = Emb)


@bot.command(aliases=["r"])
async def roll(ctx, dice: str):
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
	print(choices)
	await ctx.send(random.choice(choices))


@bot.command(aliases=["cf"])
async def coinflip(ctx):
	Coin = ["Heads", "Tails"]
	await ctx.send(random.choice(Coin))


@bot.command()
async def joined(ctx, member: discord.Member):
	if member.id == 315565100226576394:
		await ctx.send("AGrapplerNamedSam joined in 2019-11-29 04:20:20.393000")
	else:
		await ctx.send('{0.name} joined in {0.joined_at}'.format(member))


@bot.command(aliases=['ja'])
async def joinedall(ctx):
	for member in ctx.guild.members:
		await ctx.send('{0.name} joined in {0.joined_at}'.format(member))



keepAlive()
bot.run(Token)