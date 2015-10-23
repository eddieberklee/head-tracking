
from flask import Flask
from flask import render_template
app = Flask(__name__)

global whichButton
whichButton = "default_button"

@app.route("/")
def hello():
  return render_template('home.html')
  # return "Hello World!"

@app.route("/which_button")
def which_button():
  return "" + whichButton

@app.route("/button1")
def button1():
  global whichButton
  whichButton = "Button 1"
  return whichButton

@app.route("/button2")
def button2():
  global whichButton
  whichButton = "Button 2"
  return whichButton

if __name__ == "__main__":
  app.run("10.0.42.201", debug = True, threaded = True)
  whichButton = "hi"







