import telebot

BOT_TOKEN = "PASTE_YOUR_BOT_TOKEN_HERE"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "👋 Welcome to VidFetchBot!\n\n"
        "Send me a public video link.\n"
        "Supported: TikTok, Instagram, YouTube Shorts, X\n"
        "⚠️ Public videos only."
    )

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.reply_to(
        message,
        "🚧 MVP MODE\n\n"
        "Downloader logic coming next.\n\n"
        "You sent:\n" + message.text
    )

bot.infinity_polling()
