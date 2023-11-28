import telebot
bot = telebot.TeleBot('6526064986:AAHTAVAXEDLlFjEj39NTlQe1JcpPjEji_b0')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Здравствуй, пользователь. Введи "go" чтобы начать беседу.')

@bot.message_handler(commands=['go'])
def main(message):
    bot.send_message(message.chat.id, '*Мой создатель* по натуре ленивый человек, поэтому в моём арсенале всего лишь одна функция. Введи "mus", чтобы у вас была возможность послушать успокаивающую музыку.', parse_mode='Markdown')

@bot.message_handler(commands=['mus'])
def main(message):
    bot.send_message(message.chat.id, '*[Это ссылка](https://www.youtube.com/watch?v=U7FSPZdLSvM&t=89s) на музыку*,наслаждайтесь', parse_mode='Markdown')

bot.infinity_polling()