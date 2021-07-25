import json
import telegram.error
from telegram.ext import Updater, dispatcher
from telegram.ext import CommandHandler

with open('.sensdata/tokens.json') as reader:
    data = json.load(reader)
    TELEGRAM_TOKEN = data['TELEGRAM_TOKEN']

try:
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    print("Cool, you can get updates from Telegram bot")
except telegram.error.TelegramError:
    print("Oops, some Telegram error.")
except Exception:
    print("Oops, can't get updates from Telegram bot but it's not Telegram error.")

def start(update, context): # Bot action on /start command
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, write something.")

# Handlers & Dispatchers
dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start)
help_handler = CommandHandler('help', start)
settings_handler = CommandHandler('settings', start)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(settings_handler)

# Run the bot
updater.start_polling()