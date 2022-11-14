# Задача 1. Создайте программу для игры в "Крестики-нолики".
import random
def print_field(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end= ' ')
        print(' ')
def bot_stroke(matrix):
    list_empty = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == ' - ': list_empty.append([i, j])
    stroke = random.choice(list_empty)
    return stroke
def check_win(matrix):
    check = 0
    for i in range(len(matrix)):
        if matrix[i] == [' x ', ' x ', ' x ']:
            check = 1
            break
        elif matrix[i] == [' 0 ', ' 0 ', ' 0 ']:
            check = 2
            break
    for j in range(len(matrix[0])):
        if matrix[0][j] == ' x ' and matrix[1][j] == ' x ' and matrix[2][j] == ' x ':
            check = 1
            break
        elif matrix[0][j] == ' 0 ' and matrix[1][j] == ' 0 ' and matrix[2][j] == ' 0 ':
            check = 2
            break
    if matrix[0][0] == matrix[1][1] == matrix[2][2] == ' x ' or matrix[0][2] == matrix[1][1] == matrix[2][0] == ' x ':
        check = 1
       
    elif matrix[0][0] == matrix[1][1] == matrix[2][2] == ' 0 ' or matrix[0][2] == matrix[1][1] == matrix[2][0] == ' 0 ':
        check = 2
    return check
def game_over(stroke_number, game_field):
    if stroke_number > 4:
            if check_win(game_field) == 1:
                return 'You win!!!'
            elif check_win(game_field) == 2:
                return 'Bot win'
try:
    game_field = [[' - ', ' - ', ' - '], [' - ', ' - ', ' - '], [' - ', ' - ', ' - ']]
    print_field(game_field)
    stroke_number = 0
    while stroke_number < 9:
        x = int(input('Введите номер строки от 1 до 3: '))
        y = int(input('Введите номер столбца от 1 до 3: '))
        if game_field[x-1][y-1] == ' - ':
            game_field[x-1][y-1] = ' x '
            print('Вы походили:')
            print_field(game_field)
        else: print('Эта ячейка уже заполнена, ход переходит противнику')
        stroke_number += 1
        result = game_over(stroke_number, game_field)
        if result == 'You win!!!' or result == 'Bot win':
            print(result)
            break
        stroke = bot_stroke(game_field)
        game_field[stroke[0]] [stroke[1]] = ' 0 '
        print('Ход противника')
        print_field(game_field)
        stroke_number += 1
        result = game_over(stroke_number, game_field)
        if result == 'You win!!!' or result == 'Bot win':
            print(result)
            break
except: print('Something wrong')
















