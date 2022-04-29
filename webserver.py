from flask import Flask, request
from threading import Thread

import discord
from discord.ext import commands
description = "A small cute bot built by AGrapplerNamedSam."
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='?', description=description, intents=intents, case_insensitive=True)

app = Flask('')

@app.route('/')
def home():
	return "The web server is alive"

@app.route('/',methods=['POST'])
def RaspberryPi():
	if request.method == 'POST':
		bot.POSTREQUEST = "True"
		return bot.POSTREQUEST

def run():
	app.run(host='0.0.0.0',port=8080)

def stayinAlive():
	t = Thread(target=run)
	t.start()