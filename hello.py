from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
  
  os.system("open https://google.com")
  return "Hello World!"

@app.route("/John")
def John():
  return "Hello John!"

if __name__ == "__main__":
  app.run(debug=True)
