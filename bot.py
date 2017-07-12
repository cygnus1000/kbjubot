# -*- coding: utf-8 -*- 
from telegram.ext import Updater, CommandHandler

def start(bot, update):
	update.message.reply_text('Введите свой рост и вес через через слэш с точностью до десятых долей')
	update.message.reply_text('Пример - 170/66.4')
def hello(bot, update):
	update.message.reply_text(
		'Hello {}'.format(update.message.from_user.first_name))

updater = Updater('446638663:AAHkmiDnpX-YqLUrIRWOAfzIpJ4GmZZ8uB8')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()
