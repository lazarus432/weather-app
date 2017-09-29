from flask import Flask, render_template, request
import requests
app = Flask(__name__)


@app.route("/")
def index():
	return render_template("index.html")


@app.route("/temperature")
def temperature():
	return render_template('temperature.html')



if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=8000) 