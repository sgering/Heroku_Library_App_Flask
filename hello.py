from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
  
  os.system("open https://google.com")
  return "Hello World!"

@app.route("/John")
def John():
  return <a href="http://mylink.com" target="_blank">Link</a>

if __name__ == "__main__":
  app.run(debug=True)
