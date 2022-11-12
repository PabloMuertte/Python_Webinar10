from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import *

updater= Updater('5652757204:AAFwnJeMlMTrW-Ommj8Aawd7YYP2t0Uk240')

updater.dispatcher.add_handler(CommandHandler('start', start_command))
updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))
updater.dispatcher.add_handler(CommandHandler('game', game_command))
updater.dispatcher.add_handler(CommandHandler('x', input_x_command))

updater.start_polling()
updater.idle()
