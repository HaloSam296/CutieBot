import discord, asyncio
from discord.ext import commands
from discord.utils import get


description = "A small cute bot built by AGrapplerNamedSam."
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='?', description=description, intents=intents, case_insensitive=True)


def setup(bot):
	bot.add_command(togglebonk)
	bot.add_command(bonksetting)
	bot.add_command(ultimatefullbonk)
	bot.add_command(ultimatequickbonk)
	bot.add_command(quickbonksamko)
	bot.add_command(fullbonk)
	bot.add_command(quickbonk)
	bot.add_command(bonkhelp)


bot.Toggle = True
bot.x = 0
@commands.command(aliases=["tb"])
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

	
@commands.command(aliases=["bs"])
async def bonksetting(ctx):
	if bot.Toggle == True:
		await ctx.send("Bonk commands are turned on.")
	elif bot.Toggle == False:
		await ctx.send("Bonk commands are turned off.")


@commands.command(aliases=["ufb"])
async def ultimatefullbonk(ctx, samkox: discord.Member):
	if ctx.author.id == 315565100226576394:
		BonkChannel = discord.utils.get(ctx.guild.channels, id = 654535086309507083)
		await ctx.send("You've been bonked, "+samkox.mention+"!")
		await samkox.move_to(BonkChannel)


@commands.command(aliases=["uqb"])
async def ultimatequickbonk(ctx, samkox: discord.Member):
	if ctx.author.id == 315565100226576394:
		OriginalChannel = samkox.voice.channel
		BonkChannel = discord.utils.get(ctx.guild.channels, id = 654535086309507083)
		await ctx.send("You've been bonked, "+samkox.mention+"!")
		await samkox.move_to(BonkChannel)
		await asyncio.sleep(5.69)
		await samkox.move_to(OriginalChannel)


@commands.command(aliases=['qbs'])
async def quickbonksamko(ctx):
	if bot.Toggle == True:
		samkox = discord.utils.get(ctx.guild.members, id = 307353508259037185)
		BonkChannel = discord.utils.get(ctx.guild.channels, id = 654535086309507083)
		OriginalChannel = samkox.voice.channel
		await ctx.send("You've been bonked, "+samkox.mention+"!")
		await samkox.move_to(BonkChannel)
		await asyncio.sleep(6.69)
		await samkox.move_to(OriginalChannel)
	elif bot.Toggle == False:
		await ctx.send("Bonk commands are disabled")


@commands.command(aliases=["fb"])
async def fullbonk(ctx, samkox: discord.Member):
	if bot.Toggle == True:
		BonkChannel = discord.utils.get(ctx.guild.channels, id = 654535086309507083)
		if samkox.voice.self_stream or samkox.voice.self_video:
			await ctx.send(str(samkox) +" is streaming and cannot be bonked.")
			return
		else:
			await ctx.send("You've been bonked, "+samkox.mention+"!")
			await samkox.move_to(BonkChannel)
	elif bot.Toggle == False:
		await ctx.send("Bonk commands are disabled")


@commands.command(aliases=["qb"])
async def quickbonk(ctx, samkox: discord.Member):
	if bot.Toggle == True:
		OriginalChannel = samkox.voice.channel
		BonkChannel = discord.utils.get(ctx.guild.channels, id = 654535086309507083)
		if samkox.voice.self_stream or samkox.voice.self_video:
			await ctx.send(str(samkox) +" is streaming and cannot be bonked.")
			return
		else:
			await ctx.send("You've been bonked, "+samkox.mention+"!")
			await samkox.move_to(BonkChannel)
		await asyncio.sleep(5.69)
		await samkox.move_to(OriginalChannel)
	elif bot.Toggle == False:
		await ctx.send("Bonk commands are disabled")


@commands.group(invoke_without_command=True, aliases=['bh'])
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




	#https://replit.com/@HaloSam296/pythonproblems#main.py