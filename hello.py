from flask import Flask
import webbrowser

app = Flask(__name__)

@app.route("/")
def hello_world():


    webbrowser.open('http://usgs.gov')  # Go to example.com
    webbrowser.open('https://flask.palletsprojects.com/en/2.0.x/quickstart/')  # Go to example.com
    
    return "<p>Hello, World!</p>"
