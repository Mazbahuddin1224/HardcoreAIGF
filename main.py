import os
import telebot

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hey babe 😘 I'm your Sexy AI Girlfriend. Type anything 😈")

bot.polling()


Fix: Use env var for Telegram token
