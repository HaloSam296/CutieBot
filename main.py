import discord
from discord.ext import commands, tasks
import os
import logging
logging.basicConfig(level=logging.INFO)

import sys
sys.path.insert(0, 'commands/')
from webserver import keepAlive


description = "A small cute bot built by AGrapplerNamedSam."
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='?', description=description, intents=intents, case_insensitive=True)


bot.load_extension("bonk")
bot.load_extension("misc")
bot.load_extension("nick")
bot.load_extension("voice")


@bot.event
async def on_ready():
  print('Logged in as')
  print(bot.user.name)
  print("Bot ID: " + str(bot.user.id))
  print("\nTo-Do:\nMake log system\nComplete organization rework\nKeep bot cute")
  print('------')
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='HSAM BECOMING MOD 2022!')) 
#	MusicBotCheck.start()


bot.POSTREQUEST = "False"
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
	Emb.add_field(name="?schmoove '[Channel ID Here]' @[example] @[example] . . .",value="(smv) Moves a person or people into a different voice channel. The VC must be spelt accurately and must be in ''s"+' or ""s. Then ping the people you want to be moved. Do not use any commas, only spaces between the channel name and each person. NOTE: A list of the channel IDs can be found both in bot spam and music commands. I am trynig to figure out a way to allow the use of channel names instead of IDs, but it is proving difficult.',inline=True)
	Emb.set_footer(text='More commands can be added upon request!')
	await ctx.send(embed = Emb)


Token = os.environ['Token']
bot.run(Token)
keepAlive()
print("Bot is running:\n")