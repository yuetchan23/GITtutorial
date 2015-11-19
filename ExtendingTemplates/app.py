from flask import Flask, render_template  #NEW IMPORT!!

app = Flask(__name__)    #This is creating a new Flask object

#decorator that links...

@app.route('/')          								#This is the main URL
def default():
    return render_template("index.html", name = "index", title = "HOME PAGE")			#The argument should be in templates folder


@app.route('/index')          							#This is the main URL
def index():
    return render_template("index.html", name = "index", title = "HOME PAGE")			#The argument should be in templates folder


@app.route('/courses')          							#This is the main URL
def courses():
    return render_template("courses.html", name = "courses", title = "COURSES PAGE")







@app.route('/<name>')          							#This is the main URL
def home(name):
    return render_template("%s.html" % name, name = name)	#The argument should be in templates folder


if __name__ == '__main__':
    app.run(debug=True)		#debug=True is optional




