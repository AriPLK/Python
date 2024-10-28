team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
team_name1 = 'Мастера кода'
team_name2 = 'Волшебники данных'
print('В команде ' + team_name1 + ' участников: ' + str(team1_num))
print('Итого сегодня в командах участников: ' + str(team1_num) + ' и ' + str(team2_num))

print('Команда {team2} решила задач: {score}!'.format(team2=team_name2, score=score_2))
print('{team} решили задачи за {time} с!'.format(team=team_name2, time=team2_time))

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = "Победа команды Мастера кода!"
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = "Победа команды Волшебники Данных!"
else:
    result = "Ничья!"

print(f'Команды решили {score_1} и {score_2}.')
print(f'Результат битвы: {result}')
print(f'Сегодня было решено {tasks_total} и среднее время решения {time_avg} секунды на задачу!')
