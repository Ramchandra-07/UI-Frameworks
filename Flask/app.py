from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return " welcome to my website "


@app.route('/Goodbye')
def Goodbye():
    return " bye bye to my website "


app.run(debug= True)