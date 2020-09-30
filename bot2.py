import config
import telebot

bot = telebot.TeleBot(config.token)
bot.send_message(673637293, 'lol')