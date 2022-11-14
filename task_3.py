# Задача FOOTBALL необязательная: Напишите программу, которая принимает на стандартный вход список игр футбольных команд 
# с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой
# Вывод программы необходимо оформить следующим образом:
# Команда:Всегоигр Побед Ничьих Поражений Всегоочков
# Конкретный пример ввода-вывода приведён ниже.
# Порядок вывода команд произвольный.
import re
def text_in_list(text):
    list = re.split(';', text)
    return list
def count_team(list):
    unic_team = []
    for i in range(len(list)):
        if list[i][0] not in unic_team: unic_team.append(list[i][0])
        if list[i][2] not in unic_team: unic_team.append(list[i][2])
    return unic_team
def count_games(unic_team, list):
    team_and_count = []
    for e in unic_team:
        count = 0
        for i in range(len(list)):
            if e in list[i]: count += 1
        team_count = [e, count]
        team_and_count.append(team_count)
    return team_and_count
def count_win(team_all, list):
    for j in range(len(team_all)):
        count_win = 0
        count_lose = 0
        count_draw = 0
        for i in range(len(list)):
            if team_all[j][0] == list[i][0]:
                if int(list[i][1]) > int(list[i][3]): count_win += 1
                elif int(list[i][1]) < int(list[i][3]): count_lose += 1
                else: count_draw += 1
            if team_all[j][0]  == list[i][2]:
                if int(list[i][3]) > int(list[i][1]): count_win += 1
                elif int(list[i][3]) < int(list[i][1]): count_lose += 1
                else: count_draw += 1
        team_all[j].append(count_win)
        team_all[j].append(count_draw)
        team_all[j].append(count_lose)
    return team_all
def count_scores(team_all):
    for i in range(len(team_all)):
        scores = team_all[i][2]*3 + team_all[i][3]
        team_all[i].append(scores)
    return team_all
def print_array(list):
    for i in range(len(list)):
        for j in range(len(list[i])):
            print('{:^14}'.format(list[i][j]), end='|')
        print()
def fill_list():
    list = []
    n = int(input('Введите число записей: '))
    for i in range(n):
        game = input(f'Введите результаты {i+1} -й игры через ; без пробелов: ')
        list.append(text_in_list(game))
    return list
try:
    list_games = fill_list()
    teams_name = count_team(list_games)
    all_games = count_games(teams_name, list_games)
    count_all = count_win(all_games, list_games)
    result = count_scores(count_all)
    print('{:<15}'.format('Команда:'), '{:<15}'.format('Всего игр'), '{:<15}'.format('Побед'), '{:<15}'.format('Ничьих'), '{:<15}'.format('Поражений'), '{:<15}'.format('Всего очков'))
    print_array (result)
except: print('Something wrong')