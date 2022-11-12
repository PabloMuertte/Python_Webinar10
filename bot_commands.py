from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from spy_log import *
from tic_tac_toe import *

matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def start_command(update: Update, context: CallbackContext):
    log(update,context)
    update.message.reply_text(f'Here you can find main commands\n/hi\n/sum numder number\n/game (to play Tic-Tac-Toe)')

def hi_command(update: Update, context: CallbackContext):
    log(update,context)
    update.message.reply_text(f'Hi {update.effective_user.first_name}!')

def sum_command(update: Update, context: CallbackContext):
    log(update,context)
    msg = update.message.text #~input
    print(msg)
    items = msg.split() #sum 123 534543
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} + {y} = {x+y}') #~print

def game_command(update: Update, context: CallbackContext):
    log(update,context)
    update.message.reply_text('Welcome to Tic-Tac-Toe Game!\nChoose your number to input X (Input /X and your number')
    update.message.reply_text(f'[1, 2, 3]\n[4, 5, 6]\n[7, 8, 9]')

def input_x_command(update: Update, context: CallbackContext):
    log(update,context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    matrix = game(matrix_1,x,update,context)
    matrix_new = matrix
    x1 = matrix_new[0][0]
    x2 = matrix_new[0][1]
    x3 = matrix_new[0][2]
    x4 = matrix_new[1][0]
    x5 = matrix_new[1][1]
    x6 = matrix_new[1][2]
    x7 = matrix_new[2][0]
    x8 = matrix_new[2][1]
    x9 = matrix_new[2][2]
    update.message.reply_text(f'[{x1},{x2},{x3}]\n[{x4},{x5},{x6}]\n[{x7},{x8},{x9}]')
    
