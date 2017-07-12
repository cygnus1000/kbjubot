# -*- coding: utf-8 -*- 
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler

def start(bot, update):
	update.message.reply_text("Введите свой рост и вес через через слэш с точностью до десятых долей\nПример - 170/66.4")
	

def echo(bot, update):
	resp = update.message.text
	kbju = int(resp[0:2])*5-float(resp[4:])
	update.message.reply_text(kbju)
  
updater = Updater('446638663:AAHkmiDnpX-YqLUrIRWOAfzIpJ4GmZZ8uB8')
updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()