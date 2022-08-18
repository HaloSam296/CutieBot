import discord, asyncio, os#, time 
from discord.ext import commands
from discord.utils import get

description = "A small cute bot built by AGrapplerNamedSam."
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='?', description=description, intents=intents, case_insensitive=True)

def setup(bot):
	bot.add_command(addschedule)
	bot.add_command(showschedule)
	bot.add_command(removeschedule)




@commands.command(aliases=['as'])
async def addschedule(ctx, day, time, item):
	Day = day.lower()[:3]
	
	#schedule file (schedule.txt)
	SF = open('commands/weekly schedule/'+Day,'a')

	SF.write(str(time) + ' - ' + str(item) + '\n')
	await ctx.send("Item Added: \n" + str(time) + ' - ' + str(item))
	SF.close()


@commands.command(aliases=['ss'])
async def showschedule(ctx):\
	#empty file check code from StackOverflow: https://stackoverflow.com/questions/2507808/how-to-check-whether-a-file-is-empty-or-not
	S = open('commands/weekly schedule/sun','r')
	Sun = ''
	for i in S:
		Sun=Sun+i
	S.close()
	if os.stat("commands/weekly schedule/sun").st_size == 0:
		Sun="Nothing is scheduled"
		
	M = open('commands/weekly schedule/mon','r')
	Mon = ''
	for i in M:
		Mon=Mon+i
	M.close()
	if os.stat("commands/weekly schedule/mon").st_size == 0:
		Mon="Nothing is scheduled"
		
	T = open('commands/weekly schedule/tue','r')
	Tue = ''
	for i in T:
		Tue=Tue+i
	T.close()
	if os.stat("commands/weekly schedule/tue").st_size == 0:
		Tue="Nothing is scheduled"
		
	W = open('commands/weekly schedule/wed','r')
	Wed = ''
	for i in W:
		Wed=Wed+i
	W.close()
	if os.stat("commands/weekly schedule/wed").st_size == 0:
		Wed="Nothing is scheduled"
		
	T = open('commands/weekly schedule/thu','r')
	Thu = ''
	for i in T:
		Thu=Thu+i
	T.close()
	if os.stat("commands/weekly schedule/thu").st_size == 0:
		Thu="Nothing is scheduled"
		
	F = open('commands/weekly schedule/fri','r')
	Fri = ''
	for i in F:
		Fri=Fri+i
	F.close()
	if os.stat("commands/weekly schedule/fri").st_size == 0:
		Fri="Nothing is scheduled"
		
	S = open('commands/weekly schedule/sat','r')
	Sat = ''
	for i in S:
		Sat=Sat+i
	S.close()
	if os.stat("commands/weekly schedule/sat").st_size == 0:
		Sat="Nothing is scheduled"
		
	print(Sun,Mon,Tue,Wed,Thu,Fri,Sat)
	
	Emb = discord.Embed(title='Weekly Schedule (EST)',description='\n')
	Emb.add_field(name='Sunday',value=Sun, inline=False)
	Emb.add_field(name='Monday',value=Mon, inline=False)
	Emb.add_field(name='Tuesday',value=Tue, inline=False)
	Emb.add_field(name='Wednesday',value=Wed, inline=False)
	Emb.add_field(name='Thursday',value=Thu, inline=False)
	Emb.add_field(name='Friday',value=Fri, inline=False)
	Emb.add_field(name='Saturday',value=Sat, inline=False)
	Emb.set_footer(text='See `?help` for more options')
	await ctx.send(embed=Emb)





@commands.command(aliases=['rs'])
async def removeschedule(ctx, day, item):
	Day = day.lower()[:3]

	#Code from PyNative: https://pynative.com/python-delete-lines-from-file/#h-deleting-lines-matching-a-text-string
	with open('commands/weekly schedule/'+Day, "r") as input:
	    with open("commands/weekly schedule/temp.txt", "w") as output:
	        # iterate all lines from file
	        for line in input:
	            # if text matches then don't write it
	            if line.strip("\n") != item:
	                output.write(line)
	#replace old file with updated file
	os.replace('commands/weekly schedule/temp.txt', 'commands/weekly schedule/'+Day)
	await ctx.send("Process complete, it is recommended to check the schedule to confirm removal.")
	