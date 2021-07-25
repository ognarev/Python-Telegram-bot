import json
import telegram.error
from telegram.ext import Updater, dispatcher, CommandHandler
from telegram.ext.filters import Filters
from telegram.ext.messagehandler import MessageHandler

from bot_answer import get_citation

languges = ('ru', 'en')

with open('.sensdata/tokens.json') as reader:
    data = json.load(reader)
    TELEGRAM_TOKEN = data['TELEGRAM_TOKEN']
with open('data/bot_answers.json') as reader:
    bot_answers = json.load(reader)

try:
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    print("Cool, you can get updates from Telegram bot")
except telegram.error.TelegramError:
    print("Oops, some Telegram error.")
except Exception:
    print("Oops, can't get updates from Telegram bot but it's not Telegram error.")

def start_c(update, context): # reaction on /start
    context.bot.send_message(chat_id=update.effective_chat.id, text=bot_answers["start"])

def help_c(update, context): # reaction on /help
    context.bot.send_message(chat_id=update.effective_chat.id, text=bot_answers["help"])

def unknown_c(update, context): # reaction on unknown commands
    context.bot.send_message(chat_id=update.effective_chat.id, text=bot_answers["unknown"])

def message_(update, context): # reaction on text message from user
    context.bot.send_message(chat_id=update.effective_chat.id, text=get_citation(languges[0]))

# Handlers & Dispatchers
dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start_c)
help_handler = CommandHandler('help', help_c)
settings_handler = CommandHandler('settings', help_c)
message_handler = MessageHandler(~Filters.command, message_)
unknown_handler = MessageHandler(Filters.command, unknown_c)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(settings_handler)
dispatcher.add_handler(message_handler)
dispatcher.add_handler(unknown_handler) #must be last handler

# Run the bot
updater.start_polling()
updater.idle() # You can stop the bot with Ctrl+C 