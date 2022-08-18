import discord, os, sys, logging
from discord.ext import commands#, tasks
logging.basicConfig(level=logging.INFO)
sys.path.insert(0, 'commands/')
from webserver import stayinAlive#, POSTREQUEST
from misc import NewHelp

description = "A small cute bot built by AGrapplerNamedSam."
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='?', description=description, intents=intents, case_insensitive=True)

bot.load_extension("bonk")
bot.load_extension("misc")
bot.load_extension("nick")
bot.load_extension("voice")
bot.load_extension("schedule")
bot.help_command = NewHelp()

 
@bot.event
async def on_ready():
  print('Logged in as')
  print(bot.user.name)
  print("Bot ID: " + str(bot.user.id))
  print("\nTo-Do:\nMake log system\nKeep bot cute")
  print('------')
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='HSAM BECOMING MOD 2022!')) 
	

'''	MusicBotCheck.start()
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
		return'''


@bot.event
async def on_message(message):
	await bot.process_commands(message)



	

stayinAlive()
Token = os.environ['Token']
bot.run(Token)
print("Bot is running:\n")