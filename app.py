from flask import Flask,request
from telegram import Bot, Update
from telegram.ext import Dispatcher,MessageHandler,CommandHandler,Filters
import os

from main import(start,dog,cat)

app = Flask(__name__)

TOKEN = os.environ['TOKEN']
bot = Bot(TOKEN)

@app.route('/webhook', methods=['POST','GET'])
def webhook():
    
    if request.method == 'GET':
        return 'hi from Python-2022I'
    elif request.method == 'POST':
        data = request.get_json(force=True)

        update: Update = Update.de_json(data,bot)
        print(update)

        dp: Dispatcher = Dispatcher(bot,None,workers=0)

        dp.add_handler(CommandHandler('start',start))
        dp.add_handler(MessageHandler('🐶 Dog',dog))
        dp.add_handler(MessageHandler('🐈 Cat',cat))

        dp.process_update(update)
        return 'Hello'
        

    
    
    
    
    
    # # get data from request
    # data = request.get_json(force=True)

    # # update
    # update = Update.de_json(data, bot)

    # # get chat_id, text from update
    # chat_id = update.message.chat.id
    # chat = update.message
    # text = update.message.text

    # # sendMessage
    # if text != None:
    #     bot.send_message(chat_id, text)
    # print(chat)
    # return 'ok'


