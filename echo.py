#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from config import token
from random import choice
import insults

def generateInsult():
	word1 = choice(insults.word_one)
	word2 = choice(insults.word_two)
	word3 = choice(insults.word_three)
	return word1 + " " + word2 + " " + word3

def start(bot, update):
    update.message.reply_text("Greetings, ye " + generateInsult())

def help(bot, update):
    update.message.reply_text("You have to be the dumbest " + generateInsult() + " I\'ve ever laid my eyes upon.")

def echo(bot, update):
    update.message.reply_text("What\'s that, you " + generateInsult() + "?")

def main():
    updater = Updater(token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message 
    dp.add_handler(MessageHandler(Filters.text & Filters.entity(MENTION), echo))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()