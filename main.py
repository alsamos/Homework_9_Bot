from telegram import Update
from telegram.ext import Updater, Filters, CommandHandler, MessageHandler, CallbackContext
from bot_commands import *


updater = Updater('5790959562:AAFlCL0rChiHd49horY3l_#############')

updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('add', add_command))
updater.dispatcher.add_handler(CommandHandler('show', show_command))

updater.start_polling()
updater.idle()
