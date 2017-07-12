# -*- coding: utf-8 -*- 
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler

def start(bot, update):
	update.message.reply_text("Введите свой вес, рост и возраст через через слэш, вес с точностью до десятых долей\nПример - 66.4/170/20")


def echo(bot, update):
	resp = update.message.text
	l = resp.split("/")
	update.message.reply_text(9,99*int(l[0]+6,25*l[1]-4,92*l[2]-141)*0,8*1,375)
  	
updater = Updater('446638663:AAHkmiDnpX-YqLUrIRWOAfzIpJ4GmZZ8uB8')
updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))
updater.dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()
