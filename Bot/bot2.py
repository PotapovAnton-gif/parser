import config
import telebot
from make_file import file_to_csv, file_to_xlsx


bot = telebot.TeleBot(config.token)

file_start = open('/home/antpotapov2019/Bot/bot/text/Hello.txt')
file_start_content = file_start.read()

file_help = open('/home/antpotapov2019/Bot/bot/text/Help.txt')
file_help_content = file_help.read()

@bot.message_handler(commands='start')

def reply_to_start(message):
    bot.send_message(message.chat.id, file_start_content)

#@bot.message_handler(commands='help')
#
#def reply_to_help(message):
#    bot.send_message(message.chat.id, file_help_content)
#
@bot.message_handler(content_types=["text"])
def repear_all(message):
    print(message.chat.id)
    bot.send_message(message.chat.id, message.text)

   

if __name__ == "__main__":
    bot.infinity_polling()