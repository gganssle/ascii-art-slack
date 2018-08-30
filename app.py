from flask import Flask, request, jsonify
import numpy as np
import requests
from pyfiglet import Figlet

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/v20180830', methods = ['GET'])
def api():
    if request.method == 'GET':

        dictionary = {'var1':request.args.get('arg1'),
                      'var2':request.args.get('arg2')}
    return jsonify(dictionary)
# to access the above, use:
# http://127.0.0.1:5000/API?arg1=One&arg2=Two

if __name__ == '__main__':
    app.run()
