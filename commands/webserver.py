from flask import Flask, request
#import aiohttp
#from aiohttp import web
from threading import Thread

import discord
from discord.ext import commands
description = "A small cute bot built by AGrapplerNamedSam."
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='?', description=description, intents=intents, case_insensitive=True)


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