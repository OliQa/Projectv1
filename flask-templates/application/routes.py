from flask import render_template
from application import app

blogData = [
	{
		"name": {"first":"john", "last":"doe"},
		"title":"first post",
		"content":"dTTASASDTAA"
	},
	{
		"name": {"first":"oli", "last":"ok"},
		"title":"antoher post"
		
	}
]







@app.route('/home')

def home():
	return render_template('home.html', title= 'Go Home', post=blogData)



@app.route('/about')

def about():
	return render_template('about.html', title= 'About Page')


