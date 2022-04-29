import discord, random, asyncio
from discord.ext import commands
from discord.utils import get


description = "A small cute bot built by AGrapplerNamedSam."
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='?', description=description, intents=intents, case_insensitive=True)


def setup(bot):
	bot.add_command(confirm)
	bot.add_command(filth)
	bot.add_command(filthy)
	bot.add_command(roll)
	bot.add_command(choose)
	bot.add_command(coinflip)
	bot.add_command(joined)
	bot.add_command(joinedall)
	bot.add_command(aperandom)
	


@commands.command(pass_context=True)
async def confirm(ctx):
	role = get(ctx.author.guild.roles, id = 644946587000504335)
	print(role)
	f = open('logs/newlyjoined.txt','a')
	f.write('\n'+str(ctx.author)+" has joined ET.")
	f.close
	await ctx.author.add_roles(role, ctx.author)
	print(str(ctx.author)+" has been given the n00b role.\n")

  
@commands.command(aliases=['f'])
async def filth(ctx, idiot):
	await ctx.send("To hell with you, " + str(idiot) +" for that post you inferior twat. \nhttps://youtu.be/o048xeNQ3Wo") 


@commands.command(aliases=['fy'])
async def filthy(ctx):
	await ctx.send("To hell with you for that post, you inferior twat. \nhttps://youtu.be/o048xeNQ3Wo")


@commands.command(aliases=["r"])
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


@commands.command()
async def choose(ctx, *choices: str):
	print(choices)
	await ctx.send(random.choice(choices))


@commands.command(aliases=["cf"])
async def coinflip(ctx):
	Coin = ["Heads", "Tails"]
	await ctx.send(random.choice(Coin))


@commands.command()
async def joined(ctx, member: discord.Member):
	if member.id == 315565100226576394:
		await ctx.send("AGrapplerNamedSam joined in 2019-11-29 04:20:20.393000")
	else:
		await ctx.send('{0.name} joined in {0.joined_at}'.format(member))


@commands.command(aliases=['ja'])
async def joinedall(ctx):
	for member in ctx.guild.members:
		await ctx.send('{0.name} joined in {0.joined_at}'.format(member))


@commands.command(aliases=['ar'])
async def aperandom(ctx):
	Guns = ['R301','Hemlok','Flatline','Havoc','Spitfire','Devotion','Rampage','L-STAR','Bocuck','G7','Triple Take','30-30','Peacekeeper','Mastiff','EVA-8','Mozambique','Kraber','Sentinel','Charge Rifle','Longbow','CAR','R-99','Prowler','Volt','Alternator','Wingman','RE-45','P2020','none']
	GunOne = Guns[random.randint(0,len(Guns))]
	GunTwo = Guns[random.randint(0,len(Guns))]
	await ctx.send("The guns are:\n1. "+str(GunOne)+"\n2. "+str(GunTwo))


class NewHelp(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
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
          await destination.send(embed = Emb)
bot.help_command = NewHelp()