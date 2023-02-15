from flask import Flask,request
import os
from telegram import Bot, Update


app = Flask(__name__)

TOKEN = os.environ['TOKEN']
bot = Bot(TOKEN)

@app.route('/webhook', methods=['POST'])
def webhook():
    # get data from request
    data = request.get_json(force=True)

    # update
    update = Update.de_json(data, bot)

    # get chat_id, text from update
    chat_id = update.message.chat.id
    
    text = update.message.text

    # sendMessage
    if text != None:
        bot.send_message(chat_id, text)

    return 'ok'


