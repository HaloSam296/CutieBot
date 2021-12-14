import discord
from discord.ext import commands, tasks
from discord.utils import get
import os
import random
import asyncio
import logging

logging.basicConfig(level=logging.INFO)


Token = os.environ['Token']
description = "A small cute bot mostly built by AGrapplerNamedSam. VERY, VERY WIP"
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='?', description=description, intents=intents, case_insensitive=True)
bot.POSTREQUEST = "False"


@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print("Bot ID: " + str(bot.user.id))
	print('------')
#	MusicBotCheck.start()



@tasks.loop(seconds=5.0)
async def MusicBotCheck():
	if bot.POSTREQUEST == "True":
		print("DEBUG:\nMusicBotIsUp (message from Raspberry Pi on daily morning reboot): POST Request Received")
		BotSpam = bot.get_channel(889642289599754292)
		print(BotSpam)
		await BotSpam.send("Raspberry Pi has been restarted.")
		bot.POSTREQUEST = "False"
		return bot.POSTREQUEST
	if bot.POSTREQUEST == 'False':
		return	


@bot.event
async def on_message(message):
	await bot.process_commands(message)


@bot.command(pass_context=True)
async def confirm(ctx):
	role = get(ctx.author.guild.roles, name = 'n00b')
	await ctx.author.add_roles(role, ctx.author)


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
	return bot.x, bot.Toggle

	
@bot.command(aliases=["bs"])
async def bonksetting(ctx):
	if bot.Toggle == True:
		await ctx.send("Bonk commands are turned on.")
	elif bot.Toggle == False:
		await ctx.send("Bonk commands are turned off.")


@bot.command(aliases=["ufb"])
async def ultimatefullbonk(ctx, samkox: discord.Member):
	if ctx.author.id == 315565100226576394:
		BonkChannel = discord.utils.get(ctx.guild.channels, id = 654535086309507083)
		await samkox.move_to(BonkChannel)


@bot.command(aliases=["uqb"])
async def ultimatequickbonk(ctx, samkox: discord.Member):
	if ctx.author.id == 315565100226576394:
		OriginalChannel = samkox.voice.channel
		BonkChannel = discord.utils.get(ctx.guild.channels, id = 654535086309507083)
		await samkox.move_to(BonkChannel)
		await asyncio.sleep(3.5)
		await samkox.move_to(OriginalChannel)


@bot.command(aliases=['fbs'])
async def fullbonksamko(ctx):
	if bot.Toggle == True:
		samkox = discord.utils.get(ctx.guild.members, id = 307353508259037185)
		BonkChannel = discord.utils.get(ctx.guild.channels, name = "JoJo's Jail")
		await samkox.move_to(BonkChannel)
	elif bot.Toggle == False:
		await ctx.send("Bonk commands are disabled")


@bot.command(aliases=['qbs'])
async def quickbonksamko(ctx):
	if bot.Toggle == True:
		samkox = discord.utils.get(ctx.guild.members, id = 307353508259037185)
		BonkChannel = discord.utils.get(ctx.guild.channels, id = 654535086309507083)
		OriginalChannel = samkox.voice.channel
		await samkox.move_to(BonkChannel)
		await asyncio.sleep(6.69)
		await samkox.move_to(OriginalChannel)
	elif bot.Toggle == False:
		await ctx.send("Bonk commands are disabled")


@bot.command(aliases=["fb"])
async def fullbonk(ctx, samkox: discord.Member):
	if bot.Toggle == True:
		BonkChannel = discord.utils.get(ctx.guild.channels, id = 654535086309507083)
		if samkox.voice.self_stream:
			await ctx.send(str(samkox) +" is streaming and cannot be bonked.")
			return
		elif samkox.voice.self_video:
			await ctx.send(str(samkox) +" is streaming and cannot be bonked.")
		else:
			await samkox.move_to(BonkChannel)
	elif bot.Toggle == False:
		await ctx.send("Bonk commands are disabled")


@bot.command(aliases=["qb"])
async def quickbonk(ctx, samkox: discord.Member):
	if bot.Toggle == True:
		OriginalChannel = samkox.voice.channel
		BonkChannel = discord.utils.get(ctx.guild.channels, id = 654535086309507083)
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



@bot.group(invoke_without_command=True, aliases=['bh'])
async def bonkhelp(ctx):
	Emb = discord.Embed(title='Bonk Help Menu', description="The dedicated Bonk Commands help menu!")
	Emb.add_field(name='?togglebonk', value="(tb) For admins (and the bot creator) only. Toggles the bonk commands on/off.")
	Emb.add_field(name='?bonksetting', value='(bs) Displays the current toggle setting (either on or off) of the bonk commands.')
	Emb.add_field(name='?fullbonk [@example]', value='(fb) Bonk a bad boi and send them to jail! [toggled on/off]', inline=True)
	Emb.add_field(name='?quickbonk [@example]', value='(qb) Bonk a bad boi and send them to jail for five seconds! [Toggled on/off]', inline=True)
	Emb.add_field(name='?fullbonksamko', value='(fbs) Bonk a bad samko and send it to jail! [toggled on/off]', inline=True)
	Emb.add_field(name='?quickbonksamko', value='(qbs) Bonk a bad samko and send it to jail for 5 seconds! [toggled on/off]', inline=True)
	Emb.add_field(name='?ultimatefullbonk', value="(ufb)\n :).", inline=True)
	Emb.add_field(name='?ultimatequickbonk', value="(uqb)\n :).", inline=True)
	await ctx.send(embed = Emb)


bot.remove_command("help")
@bot.group(invoke_without_command=True)
async def help(ctx):
	Emb = discord.Embed(title='Help Menu',description='The Help Menu. Ask AGrapplerNamedSam or a mod for more help.')
	Emb.add_field(name='?roll [NdN]', value='Rolls a set of dice.', inline = True)
	Emb.add_field(name='?choose [arg1, arg2, ...]', value='Randomly chooses between a set of options.', inline =True)
	Emb.add_field(name='?coinflip', value='Do I really need to explain this one?', inline = True)
	Emb.add_field(name='?joined [@user#0000]', value='Displays when a user has joined the server.', inline = True)
	Emb.add_field(name='?bonkhelp', value = '(bh) Displays the help menu showing all bonk commands.', inline=True)
	#Emb.add_field(name='?playlisthelp',value='(plh) Displays the help menu showing all avaailable playlists. (Yes, ph was the original shortcut. Yes, I very quickly changed that.)', inline=True)
	Emb.add_field(name='?joinedall', value="Lists when every member (bots included) joined the server. Exports a LOT of text, do NOT use to spam and do NOT use outside #bot-spam!")
	Emb.add_field(name='?filth [@example]', value="(f) Sends a very appropriate response to whoever is pinged.", inline=True)
	Emb.add_field(name='?lazydj [VC ID (look at music command pins)]', value="(ldj) I'm a lazy DJ. This automatically queues up my playlist and then shuffles it. (Currently CutieBot must join a VC to summon and queue the bot. I am in the process of trying to figure out a workaround, please excuse how annoying this can be for now. I'm also trying to make it easier to use than the channel IDs, because that is not user friendly at all lol)", inline=True)
	Emb.add_field(name='?join',value="(j) Joins the voice channel of whoever sent the command. NOTE: CutieBot CANNOT play any sound, this and the leave command are here for the commands that work with the music bot.",inline=True)
	Emb.add_field(name='?leave',value="(l) Leaves the current voice channel CutieBot is in. NOTE: CutieBot CANNOT play any sound, this and the join command are here for the commands that work with the music bot.",inline=True)
	Emb.add_field(name="?schmoove '[Channel ID Here]' @[example] @[example] . . .",value="(shmv) Moves a person or people into a different voice channel. The VC must be spelt accurately and must be in ''s"+' or ""s. Then ping the people you want to be moved. Do not use any commas, only spaces between the channel name and each person. NOTE: A list of the channel IDs can be found both in bot spam and music commands. I am trynig to figure out a way to allow the use of channel names instead of IDs, but it is proving difficult.',inline=True)
	Emb.set_footer(text='More commands can be added upon request!')
	await ctx.send(embed = Emb)


'''
@bot.group(invoke_without_command=True, aliases=['plh'])
async def playlisthelp(ctx):
	Emb = discord.Embed(title='Playlist Help Menu',description='The help menu for all the playlist shortcuts!')
	Emb.add_field(name='',value='', inline=True)
	Emb.set_footer(text='')
	await ctx.send(embed = Emb)
'''


@bot.command(aliases=['j'])
async def join(ctx):
	VC = ctx.author.voice.channel
	await VC.connect()


@bot.command(aliases=['l'])
async def leave(ctx):
	await ctx.voice_client.disconnect()


@bot.command(aliases=['smv'])
async def schmoove(ctx, ChannelID, *args: discord.Member):
	Destination = discord.utils.get(ctx.guild.channels, id = int(ChannelID))
	for user in args:
		await user.move_to(Destination)
		await ctx.send(str(user)+" has been sent to: " + str(Destination))


@bot.command()
async def taco(ctx):
	MusicChannel = discord.utils.get(ctx.guild.channels, id = 590668662298640395)
	VC = ctx.author.voice.channel
	await VC.connect()
	await MusicChannel.send("!join")
	await asyncio.sleep(1.5)
	await MusicChannel.send('!play https://youtu.be/wjeoEjI6g8Q')
	await ctx.voice_client.disconnect()


@bot.command(aliases=['ntldj'])
async def nametestlazydj(ctx, Channel):
	print(Channel)
	MusicChannel = discord.utils.get(ctx.guild.channels, id = 590668662298640395)
	VC = discord.utils.get(ctx.guild.channels, name = Channel)
	print(VC)
	await  VC.connect()
	await MusicChannel.send("!join")
	await asyncio.sleep(1.5)
	await MusicChannel.send('!play https://open.spotify.com/playlist/1cUk2WTot6bbRnAVMzJ1kQ?si=d9da271f67a9458c')
	await asyncio.sleep(120)	
	await MusicChannel.send("!shuffle")
	await ctx.voice_client.disconnect()


@bot.command(aliases=['ldj'])
async def lazydj(ctx, ChannelID):
	MusicChannel = discord.utils.get(ctx.guild.channels, id = 590668662298640395)
	VC = discord.utils.get(ctx.guild.channels, id = int(ChannelID))
	await  VC.connect()
	await MusicChannel.send("!join")
	await asyncio.sleep(1.5)
	await MusicChannel.send('!play https://open.spotify.com/playlist/1cUk2WTot6bbRnAVMzJ1kQ?si=d9da271f67a9458c')
	await asyncio.sleep(120)	
	await MusicChannel.send("!shuffle")
	await ctx.voice_client.disconnect()


@bot.command(aliases=['ssldj'])
async def selfsummonlazydj(ctx):
	MusicChannel = discord.utils.get(ctx.guild.channels, id = 590668662298640395)
	VC = ctx.author.voice.channel
	await VC.connect()
	await MusicChannel.send("!join")
	await asyncio.sleep(1.5)
	await MusicChannel.send('!play https://open.spotify.com/playlist/1cUk2WTot6bbRnAVMzJ1kQ?si=d9da271f67a9458c')
	await asyncio.sleep(120)	
	await MusicChannel.send("!shuffle")
	await ctx.voice_client.disconnect()


@bot.command(aliases=['f'])
async def filth(ctx, idiot):
	await ctx.send("To hell with you, " + str(idiot) +" for that post you inferior twat. \nhttps://youtu.be/o048xeNQ3Wo") 


@bot.command(aliases=['fy'])
async def filthy(ctx):
	await ctx.send("To hell with you for that post, you inferior twat. \nhttps://youtu.be/o048xeNQ3Wo")


@bot.command(aliases=["r"])
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



from flask import Flask, request
#import aiohttp
#from aiohttp import web
from threading import Thread

'''Need to migrate from requests to aiohttp sometime, just very difficult, POST is much more complicated. Reason for migration is that request is a blocker, it pauses the bot and does not let anything else run, even if the bot is given a command. Asynchronous functions (async def MyFunctino(args)) are what allows commands to be queued with multiples at a time, hence why they are used and called over normal 
functions. In an unlucky occasion, using regular, non asynchronous commands could cause the bot to run into an error.'''


app = Flask(
	"CutieBot",
	template_folder = 'HTML',
	static_folder='static'
	)


@app.route('/')
def home():
	return "The web server is live"


@app.route('/',methods=['POST'])
def RaspberryPi():
	if request.method == 'POST':
		bot.POSTREQUEST = "True"
		return bot.POSTREQUEST


def run():
	app.run(host='0.0.0.0',port=8080)


def keepAlive():
	t = Thread(target=run)
	t.start()


keepAlive()
bot.run(Token)