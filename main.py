import discord
from discord.ext import commands, tasks
from discord.utils import get
import os
import random
import asyncio
#from StayinAlive import keepAlive


Token = os.environ['Token']
description = "A small cute bot mostly built by AGrapplerNamedSam. VERY, VERY WIP"
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='?', description=description, intents=intents)
bot.POSTREQUEST = "False"


@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print("Bot ID: " + str(bot.user.id))
	print('------')
#	MusicBotCheck.start()


#THIS BLOODY THING TOOK SO MUCH WORK, FOR MORE THAN IT HAD ANY RIGHT
#THE RASPBERRY PI WAS FIGHTING ME JUST AS MUCH AS THE CODE
'''@tasks.loop(seconds=60.0)
async def MusicBotCheck():
	if bot.POSTREQUEST == "True":
		print("DEBUG:\nMusicBotIsUp (message from Raspberry Pi on daily morning reboot): POST Request Received")
		BotSpam = bot.get_channel(889642289599754292)
		print(BotSpam)
		await BotSpam.send("Raspberry Pi has been restarted.")
		bot.POSTREQUEST = "False"
		return bot.POSTREQUEST
	if bot.POSTREQUEST == 'False':
		return	'''


@bot.command(pass_context=True)
async def confirm(ctx):
	role = get(ctx.author.guild.roles, name = 'n00b')
	await ctx.author.add_roles(role, ctx.author)


#THIS IS COMMENTED OUT, THIS WILL NOT RUN EVEN IF A USER CALLS THE COMMAND 
#(RUNS THE COMMAND). IT IS LEFT IN JUST IN CASE OF GREAT NEED. A NUCLEAR
#OPTION, ONE MIGHT SAY ;)
'''@bot.command()
async def beannoying(ctx):
  await ctx.send('@everyone')
'''

@bot.event
async def on_message(message):
	if message.author == bot.user:
		return
	message.content = message.content.lower()
	if "sophie" in message.content:
		await message.channel.send("Wow, that Sophie person sounds like such a cutie!")


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
		await ctx.send("ERROR @AGrapplerNamedSam#5801, bonksetting has failed. Somehow?!")


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


'''
Below is the code for the Flask webserver that keeps the bot alive. It was originally 
in a seperate, neater file, however I also run a music bot locally on a raspberry pi 
with scheduled daily reboots, and I want CutieBot to notify me whenever a reboot 
happens (so I can know everything is going okay with it). Therefore, for the time being 
I have moved the flask server here so that it is much easier for the variables and 
requests to interact between the webserver and the Discord functions. I will leave the 
original web server file for a more lightweight and basic solution if someone wants it, 
however without any change the code below will be what runs the web server.
'''
'''
from flask import Flask, request, render_template
#import aiohttp
#from aiohttp import web
from threading import Thread

Need to migrate from requests to aiohttp sometime, just very difficult, POST is
much more complicated. Reason for migration is that request is a blocker, it pauses the bot and does not let anything else run, even if the bot is given a command. 
Asynchronous functions (async def MyFunctino(args)) are what allows commands to be
queued with multiples at a time, hence why they are used and called over normal 
functions.


app = Flask("CutieBot")

	template_folder = 'HTML',
	static_folder='static'
	)

@app.route('/')
def home():
	return "The web server is live"
	#return render_template('index.html')

@app.route('/',methods=['POST'])
def RaspberryPi():
	if request.method == 'POST':
		bot.POSTREQUEST = "True"
		return bot.POSTREQUEST

def run():
	app.run(host='0.0.0.0',port=8080)

#As the name suggests, this great function is the lifeblood of keeping the bot running 
#even while all browsers are closed.
def keepAlive():
	t = Thread(target=run)
	t.start()
'''





from flask import Flask
from threading import Thread

app = Flask('CutieBot')

@app.route('/')
def home():
	return "The web server is live and the bot is running."

def run():
	app.run(host='0.0.0.0',port=8080)

def keepAlive():
	t = Thread(target=run)
	t.start()


keepAlive()
bot.run(Token)
