import discord
from discord.ext import commands
from discord.utils import get
import random
import asyncio


description = "A small cute bot built by AGrapplerNamedSam."
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='?', description=description, intents=intents, case_insensitive=True)


def setup(bot):
	bot.add_command(changeghillinick)
	bot.add_command(changejojonick)
	bot.add_command(funi)
	bot.add_command(changesamkonick)
	bot.add_command(resetsamkonick)
	bot.add_command(togglesamkonick)
	bot.add_command(samkorandomnick)
	bot.add_command(samkorandomnickcount)
	

@commands.command(aliases=['cgn'])
async def changeghillinick(ctx, nn):
	ghilli = discord.utils.get(ctx.guild.members, id = 254770612747108364)
	await ghilli.edit(nick=nn)


@commands.command(aliases=['cjn'])
async def changejojonick(ctx, nn):
	jojo = discord.utils.get(ctx.guild.members, id = 460841388859195402)
	await jojo.edit(nick=nn)


@commands.command()
async def funi(ctx):
	await togglesamkonick(ctx)
	await samkorandomnick(ctx)


@commands.command(aliases=['csn','snc','nsc','cns','ncs','scn'])
async def changesamkonick(ctx, nn):
	samko = discord.utils.get(ctx.guild.members, id = 307353508259037185)
	await samko.edit(nick=nn)
	f = open('logs/samkonicks.txt', 'a')
	f.write(nn+'\n')
	f.close


@commands.command(aliases=['rsn'])
async def resetsamkonick(ctx):
	samko = discord.utils.get(ctx.guild.members, id = 307353508259037185)
	await samko.edit(nick="SamkoX")


bot.y=0
@commands.command(aliases=['tsn'])
async def togglesamkonick(ctx):
	bot.y = bot.y+1
	print("Bot.y changed to: "+str(bot.y))
	if bot.y % 2 == 0:
		await ctx.send("Samko Random Nick toggled off.")
	if bot.y % 2 == 1:
		await ctx.send("Samko Random Nick toggeled on.")
	return bot.y


@commands.command(aliases=["srn"])
async def samkorandomnick(ctx):
	print("Loop")
	samko = discord.utils.get(ctx.guild.members, id = 307353508259037185)
	samkonicks = ['Baby Canada','Smako','Samko','Smeggo','SMEGALOX SUPREME', "*scmedemonic screeching*", 'Smeegle', 'Smeegolox','Smegma', 'Smeglox', 'SMEGLOX SUPREME', 'Samuel Ko', 'smoogle', 'Samuel Canada', 'Canadia Boy', 'Maple Boy','Moose Child', 'Samko','Samko','Samko','Samko','Samko','Samoose','smoose','§@ƜƘΘ™','','smak', 'good canadian','sheckle supreme','le moose']
	x = 0
	while bot.y % 2 == 1:
		x = x+1
		print(x)
		listpos = random.randint(0, len(samkonicks)-1)
		nn = samkonicks[listpos]
		await samko.edit(nick=nn)
		f = open('logs/samkonicks.txt', 'a')
		f.write(nn+'\n')
		f.close
		await asyncio.sleep(300)


#this took way too much work, fml
@commands.command(aliases=['rnc'])
async def samkorandomnickcount(ctx):
	nicklist = []
	nickranlist = []
	f = open('logs/samkonicks.txt','r')

	for i in f:
		x = 0
		i = i.replace('\n','')

		if i in nickranlist:
			print(str(i)+" is already counted. Passed.")

		else:
			g = open('logs/samkonicks.txt','r')

			for y in g:
				y = y.replace('\n','')
				print("i: ." +i+ ".\n" +"y: ." +y+ '.')

				if y == i:
					x = x + 1
					print("Duplicate found, x is now: "+str(x)+'\n')

				else:
					print("pass\n")

			nicklist.append(str(i)+": "+str(x))
			print(str(x)+" added to "+str(i)+'\n')

		nickranlist.append(str(i))
		print("current nicklist: "+str(nicklist)+'\n\n')

	print("Final NickList: "+str(nicklist))
	print(range(len(nicklist)))
	finalmessage = 'Samko nickname count:\n'

	for z in range(len(nicklist)):
		finalmessage = finalmessage+nicklist[z]+'\n'

	print(finalmessage)		
	await ctx.send(finalmessage)