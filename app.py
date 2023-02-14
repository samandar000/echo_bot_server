from flask import Flask
import os
import requests





app = Flask(__name__)

TOKEN = os.environ['TOKEN']

@app.route('/webhook',methods=['GET'])
def webhook():
     
    data = requests.get_json(force=True)

    print(data)

    return 'ok'


