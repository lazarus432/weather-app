from flask import Flask, render_template, request
import requests
app = Flask(__name__)


@app.route("/")
def index():
	return render_template("index.html")


@app.route("/temperature", methods = ['POST'])
def temperature():
	city = request.form['city']
	r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city + ',&appid=49f75f46bfbc60e9a7edf7760cc11716')
	result = r.json()
	return str(result)
	#return render_template('temperature.html')



if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=8000) 