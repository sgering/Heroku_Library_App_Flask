from flask import Flask
import webbrowser

app = Flask(__name__)

@app.route("/")
def hello_world():


    webbrowser.open_new_tab('http://usgs.gov')  # Go to example.com
    webbrowser.open_new_tab('https://flask.palletsprojects.com/en/2.0.x/quickstart/')  # Go to example.com
    
    return webbrowser.open_new_tab('http://usgs.gov')
