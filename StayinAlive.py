from flask import Flask
from threading import Thread

app = Flask('CutieBot')

@app.route('/')
def home():
	return "The web server is live and the bot is running."

def run():
	app.run(host='0.0.0.0',port=8080, debug=True)

def keepAlive():
	t = Thread(target=run)
	t.start()

