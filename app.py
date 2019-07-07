from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse, Message
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
import urllib, random, csv


app = Flask(__name__)

twilio_host='0.0.0.0'
twilio_port = 80

def rand():
    with open(r'truisms.csv') as f:
        reader = csv.reader(f)
        chosen_row = random.choice(list(reader))
        chosen_row = ' '.join(chosen_row)
    return(chosen_row)

@app.route("/sms", methods=['GET', 'POST'])
def sms():
    #client = Client(account_sid, auth_token)
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
    return "DJC About page.  :)"

'''
if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=5000, debug=True)
    app.run(host=twilio_host, port=twilio_port, debug=True)
'''
