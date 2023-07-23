from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "llo2ay"
password = "123"
facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina","jiana", "rani", "carlos", "nimer"]


@app.route("/",methods=['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		name=request.form["username"]
		pas=request.form["password"]
		if name == username and pas == password: 

			return redirect(url_for('home'))

	return render_template('login.html')

@app.route("/home",methods=['GET', 'POST'])  # '/' for the default page
def home():
	if request.method == 'GET':
		return render_template('home.html',facebook_friends=facebook_friends)
	else:
		print("hi")
# print(facebook_friends)



@app.route("/friend_exists/<string:name>",methods=['GET', 'POST'])  # '/' for the default page
def exi(name):
		if name in facebook_friends:
			leshem = True 
		else:
			leshem = False
		return render_template('friend_exists.html',name=name,leshem=leshem)


	  		  



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
	debug=True
	)








