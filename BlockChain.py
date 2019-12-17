import json
from flask import Flask, request
from User import verify
import globalaccount
import globalvar

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World'


@app.route('/getblock')
def getblock():
    return json.dumps(globalvar.block_list)


@app.route('/submittrans')
def submittrans():
    data = {}
    data['from'] = request.args.get('from')
    data['to'] = request.args.get('to')
    data['num'] = int(request.args.get('num'))
    data['flg'] = int(request.args.get('flg'))
    sig = request.args.get('sig')
    if float(data['num']) > globalaccount.get_number(data['from']):
        return "Insufficient balance"
    if globalaccount.get_flg(data['from'], data['flg']):
        return "Transaction flag is wrong"
    if verify(data['from'], str(data), sig) is False:
        return "Wrong Signature"
    data['sig'] = sig
    globalvar.append_trans(data)
    return "transaction submitted successfully"


if __name__ == '__main__':
    globalaccount._init()
    app.run(debug=False, port=8000)

