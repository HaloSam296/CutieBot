import discord, asyncio#, time 
from discord.ext import commands
from discord.utils import get

description = "A small cute bot built by AGrapplerNamedSam."
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='?', description=description, intents=intents, case_insensitive=True)

def setup(bot):
	bot.add_command(addschedule)

bot.scheduleEmb = discord.Embed(title='Weekly Schedule')


@commands.command(aliases=['as'])
async def addschedule(ctx, day, time, item):
	Day = day.lower()[:3]
	return Day
	
	#schedule file (schedule.txt)
	SF = open('commands/weekly schedule/'+Day,'a')

	SF.write('\n' + str(time) + ' - ' + str(item))
	await ctx.send("Item Added: \n" + str(time) + ' - ' + str(item))
	
	SF.close()
