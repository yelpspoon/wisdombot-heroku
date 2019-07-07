from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse, Message
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
import urllib, random, csv


app = Flask(__name__)

def rand():
    with open(r'truisms.csv') as f:
        reader = csv.reader(f)
        chosen_row = random.choice(list(reader))
        chosen_row = ' '.join(chosen_row)
    return(chosen_row)

@app.route("/sms", methods=['GET', 'POST'])
def sms():
    F = request.values.get('From')
    T = request.values.get('To')
    B = request.values.get('Body')
    message = '{0} From: {1} -> {2}'.format(B, F, rand() )

    print(message)
    resp = MessagingResponse()
    resp.message(message)
    return str(resp)

@app.route("/")
def hello():
    return "Hello World! goto /sms"

@app.route("/about")
def about():
    return "The About page.  :)"
