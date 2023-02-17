from telegram import Update,ReplyKeyboardMarkup,KeyboardButton
from telegram.ext import CallbackContext,Updater
import requests


def start(update,context):
    text = 'Welcome to our bot\n\npress the button for dog photo and cet '

    keyboard = [[KeyboardButton('🐶 Dog'),KeyboardButton('🐈 Cat')]]

    update.message.reply_text(text,reply_markup=ReplyKeyboardMarkup(keyboard,resize_keyboard=True))

def dog(update: Update, context: CallbackContext):
    r = requests.get('https://random.dog/woof.json')
    url = r.json()['url']
    update.message.reply_photo(url)




def cat(update: Update, context: CallbackContext):
    r = requests.get('https://aws.random.cat/meow')
    url = r.json()['file']
    update.message.reply_photo(url)