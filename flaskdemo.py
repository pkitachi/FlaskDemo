from flask import Flask,render_template,url_for
app = Flask(__name__)

posts = [
	{
		'author':'Author 1',
		'content':'Content 1',
		'title':'Title 1',
		'date_posted':'April 18 20XX'
	},
	{
		'author':'Author 2',
		'content':'Content 2',
		'title':'Title 2',
		'date_posted':'May 19 20XX'
	}
]

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html',posts=posts)


@app.route("/about")
def about():
	return render_template('about.html')


@app.route("/login")
def login():
	return render_template('login.html')


@app.route("/register")
def register():
	return render_template('register.html')

if __name__ == '__main__':
	app.run(debug=True)