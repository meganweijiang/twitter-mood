#!flask/bin/python

import os

from flask import Flask, render_template, request, redirect, url_for
from app.gettweets import *
from app.getemotions import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    author = "Megan Weijiang & Tiffany Tso"
    name = "TwitterMood"
    return render_template('index.html', author=author, name=name)

@app.route('/search', methods=['GET'])
def search():
	name = "Results"
	twitter_query = request.args.get('search_query')
	try:
		api_inst = getInst()
		jsonList = getData(api_inst, twitter_query)
	except:
		return render_template('error.html', name='Error')
	try:
		toneList = getTones(jsonList)
		vals = getAvg(toneList)
		return render_template('search.html', data=json.dumps(vals), name=name)
	except:
		return render_template('error.html', name='Error')

@app.route('/about', methods=['GET'])
def about():
	name = "About"
	return render_template('about.html', name=name)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)