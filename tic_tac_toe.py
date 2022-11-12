"""
    Создайте программу для игры в ""Крестики-нолики"".
"""
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from random import randint


def random_O(matrix):
    O = randint(1,9)
    for i in range (3):
        for j in range (3):
            if matrix[i][j] == O:
                matrix[i][j] = str('O')
                return matrix

def find_item_x (matrix,x):
    for i in range (0,3):
        for j in range (0,3):
            if matrix[i][j] == x:
                matrix[i][j] = str('X')
    return matrix



def winer_check(matrix_1,c,update: Update, context: CallbackContext):

    if matrix_1[0][0]==matrix_1[0][1]==matrix_1[0][2]:
        if c==1:
            winner = update.effective_user.first_name
            update.message.reply_text(f'Winner is {winner}!')
            matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        elif c==2:
            winner = 'Bot'
            update.message.reply_text(f'Winner is {winner}!')
            matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    elif matrix_1[1][0]==matrix_1[1][1]==matrix_1[1][2]:
        if c==1:
            winner = update.effective_user.first_name
            update.message.reply_text(f'Winner is {winner}!')
            matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        elif c==2:
            winner = 'Bot'
            update.message.reply_text(f'Winner is {winner}!')
            matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    elif matrix_1[2][0]==matrix_1[2][1]==matrix_1[2][2]:
        if c==1:
            winner = update.effective_user.first_name
            update.message.reply_text(f'Winner is {winner}!')
            matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        elif c==2:
            winner = 'Bot'
            update.message.reply_text(f'Winner is {winner}!')
            matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    elif matrix_1[0][0]==matrix_1[1][0]==matrix_1[2][0]:
        if c==1:
            winner = update.effective_user.first_name
            update.message.reply_text(f'Winner is {winner}!')
            matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        elif c==2:
            winner = 'Bot'
            update.message.reply_text(f'Winner is {winner}!')
            matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    elif matrix_1[0][1]==matrix_1[1][1]==matrix_1[2][1]:
        if c==1:
            winner = update.effective_user.first_name
            update.message.reply_text(f'Winner is {winner}!')
            matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        elif c==2:
            winner = 'Bot'
            update.message.reply_text(f'Winner is {winner}!')
            matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    elif matrix_1[0][2]==matrix_1[1][2]==matrix_1[2][2]:
        if c==1:
            winner = update.effective_user.first_name
            update.message.reply_text(f'Winner is {winner}!')
            matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        elif c==2:
            winner = 'Bot'
            update.message.reply_text(f'Winner is {winner}!')
            matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    elif matrix_1[0][0]==matrix_1[1][1]==matrix_1[2][2]:
        if c==1:
            winner = update.effective_user.first_name
            update.message.reply_text(f'Winner is {winner}!')
            matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        elif c==2:
            winer = 'Bot'
            update.message.reply_text(f'Winner is {winner}!')
            matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    elif matrix_1[2][0]==matrix_1[1][1]==matrix_1[0][2]:
        if c==1:
            winner = update.effective_user.first_name
            update.message.reply_text(f'Winner is {winner}!')
            matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        elif c==2:
            winner = 'Bot'
            update.message.reply_text(f'Winner is {winner}!')
            matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def game (matrix_1,x,update: Update, context: CallbackContext):
            matrix = find_item_x(matrix_1,x)
            c = 1
            winer_check(matrix,c,update, context)
            matrix = random_O(matrix)
            c=2
            winer_check(matrix,c,update, context)
            return matrix     




