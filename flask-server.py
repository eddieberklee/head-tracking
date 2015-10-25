
from flask import Flask
from flask import render_template
app = Flask(__name__)

global whichButton
whichButton = "default_button"

@app.route("/")
def hello():
  return render_template('index.html')
  # return "Hello World!"

@app.route("/which_button")
def which_button():
  return "" + whichButton

@app.route("/button1")
def button1():
  global whichButton
  whichButton = "1"
  return whichButton

@app.route("/button2")
def button2():
  global whichButton
  whichButton = "2"
  return whichButton

@app.route("/button3")
def button3():
  global whichButton
  whichButton = "3"
  return whichButton

@app.route("/button4")
def button4():
  global whichButton
  whichButton = "4"
  return whichButton

@app.route("/button5")
def button5():
  global whichButton
  whichButton = "5"
  return whichButton

@app.route("/button6")
def button6():
  global whichButton
  whichButton = "6"
  return whichButton

@app.route("/button7")
def button7():
  global whichButton
  whichButton = "7"
  return whichButton

if __name__ == "__main__":
  app.run("10.0.42.201", debug = True, threaded = True)
  # app.run(debug = True, threaded = True)
  # app.run("192.168.1.245", debug = True, threaded = True)
  whichButton = "hi"







