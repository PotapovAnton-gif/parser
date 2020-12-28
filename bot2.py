import config
import telebot
import 

bot = telebot.TeleBot(config.token)

file_start = open('/home/antpotapov2019/Bot/bot/Hello.txt')
file_start_content = file_start.read()

file_help = open('/home/antpotapov2019/Bot/bot/Help.txt')
file_help_content = file_help.read()

@bot.message_handler(commands='start')

def reply_to_start(message):
    bot.send_message(message.chat.id, file_start_content,reply_markup=keyboard1)

@bot.message_handler(commands='help')

def reply_to_help(message):
    bot.send_message(message.chat.id, file_help_content)

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Ввести URL', 'Поставить оценку')

@bot.message_handler(content_types = 'text')

def reply_to_

if __name__ == "__main__":
    bot.infinity_polling()