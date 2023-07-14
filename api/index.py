from flask import Flask
import random
import string
import tls_client

app = Flask(__name__)

def randomStringDigits(stringLength=6):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

@app.route('/')
def home():
    session = tls_client.Session(
    client_identifier='safari_ios_15_6',
    random_tls_extension_order=True
    )
    return str(session)

@app.route('/about')
def about():
    return 'About'
