import discord, asyncio
from discord.ext import commands
from discord.utils import get


description = "A small cute bot built by AGrapplerNamedSam."
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='?', description=description, intents=intents, case_insensitive=True)


def setup(bot):
	bot.add_command(join)
	bot.add_command(leave)
	bot.add_command(schmoove)
	bot.add_command(lazydj)


@commands.command(aliases=['j'])
async def join(ctx):
	VC = ctx.author.voice.channel
	await VC.connect()


@commands.command(aliases=['l'])
async def leave(ctx):
	await ctx.voice_client.disconnect()


@commands.command(aliases=['smv'])
async def schmoove(ctx, ChannelName, *args: discord.Member):
	Destination = discord.utils.get(ctx.guild.channels, name = ChannelName)
	for user in args:
		await user.move_to(Destination)
		await ctx.send(str(user)+" has been sent to: " + str(Destination))


@commands.command(aliases=['ldj'])
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