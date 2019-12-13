import json
from flask import Flask, request
from User import verify

app = Flask(__name__)
block_list = {1: 1, 2: {'zc': 'adf', 'zc2': 'fad'}, 3: "aaa"}


@app.route('/')
def index():
    return 'Hello World'


@app.route('/getblock')
def getblock():
    return json.dumps(block_list)


@app.route('/submittrans')
def submittrans():
    start = request.args.get('from')
    end = request.args.get('to')
    num = request.args.get('num')
    flg = request.args.get('flg')
    sig = request.args.get('sig')
    if flg != account_flg[start]:
        return "Transaction flag is wrong"
    if num > account_number[start]:
        return "Insufficient account balance"
    if sig !=
"

if __name__ == '__main__':
    app.run(debug=True, port=8000)

