from flask import Flask

app = Flask(__name__)

def randomStringDigits(stringLength=6):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

@app.route('/')
def home():
    cache = str(randomStringDigits(12))
    return cache

@app.route('/about')
def about():
    return 'About'
