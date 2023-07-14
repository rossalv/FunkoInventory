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
    pid = 70876
    session = tls_client.Session(
    client_identifier='safari_ios_15_6',
    random_tls_extension_order=True
        )
    lo = 0
    hi = 20000
    lastmid = -1
    data = {}
    while True:
        mid = (lo + hi) // 2
        if mid == lastmid:
            stock = mid
            break
        cache = randomStringDigits(12)
        page = session.get('https://funko.com/on/demandware.store/Sites-FunkoUS-Site/en_US/Product-ShowQuickView?pid=' + str(pid) + '&quantity=' + str(mid) + '&cache=' + cache)
        data = page.json()
        availability = data['product']['availability']['messages'][0]
        lastmid = mid
        if availability == 'This item is currently not available':
            stock = '0'
            #print(f'Stock: {stock}')
            break
        elif availability == '*** Item(s) in Stock':
            hi = mid
        else:
            lo = mid

    name = str(data['product']['productName'])
    price = str(data['product']['price']['sales']['formatted'])
    produrl = 'https://funko.com/ralvin/' + str(pid) + '.html'
    return f'{name} - {stock}'

@app.route('/about')
def about():
    return 'About'
