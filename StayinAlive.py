from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
	return "You found the easter egg within my code, send me a screenshot of this mini-webpage to get my appreciation! (btw, the bot is running lol)"

def run():
	app.run(host='0.0.0.0',port=8080)

def keepAlive():
	t = Thread(target=run)
	t.start()

