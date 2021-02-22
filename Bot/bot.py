import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def repear_all(message):
    print(message.chat.id)
    bot.send_message(message.chat.id, message.text)

if __name__ == "__main__":
    bot.infinity_polling()




