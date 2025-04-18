
import telebot

TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_message = message.text.strip().lower()
    # Simple language-based detection (English default)
    if 'hi' in user_message or 'hello' in user_message:
        reply = "💋 I’m all yours tonight... Wanna see more? 😈 [Click here](https://tinyurl.com/4y6xvezz)"
    else:
        reply = "🔥 I'm burning for you... come closer 👉 [Click here](https://tinyurl.com/4y6xvezz)"
    bot.send_message(message.chat.id, reply, parse_mode='Markdown')

bot.polling()
