from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
import json
import requests
import time
import unidecode

app = Flask(__name__);

ask = Ask(app,"/xLuisApp")

@ask.launch
def start_skill():
    welcome_message = "Hello Luis How are you?"
    return question(welcome_message)

@ask.intent("GoodIntent")
def share_headlines():
    return statement("Thats good")
@ask.intent("BadIntent")
def no_intent():
    bye_text = "Okay..."
    return statement(bye_text)

if __name__ == "__main__":
    app.run(debug=True);
