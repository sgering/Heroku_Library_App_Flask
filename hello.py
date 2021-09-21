from flask import Flask
import webbrowser

app = Flask(__name__,template_folder="templates")

@app.route("/")
def hello_world():


    webbrowser.open_new_tab('http://usgs.gov')  # Go to example.com
    webbrowser.open_new_tab('https://flask.palletsprojects.com/en/2.0.x/quickstart/')  # Go to example.com
    
    return "<p>Hello, World!</p>"
