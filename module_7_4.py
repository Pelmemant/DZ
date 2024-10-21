time1_name = "Мастера кода"
time2_name = "Волшебники данных"
team1_num = str(5)
team2_num = str(6)
score_1 = str(40)
score_2 = str(42)
team1_time = str(1552.512)
team2_time = str(2153.314)
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = "победа команды Волшебники Данных!"
else:
    result = "ничья!"
task_total = int(score_1) + int(score_2)
time_avg = round((float(team1_time)+float(team2_time)/(task_total)), 3)

print("В команде Мастера кода участников: %s" % team1_num)
print('Итого сегодня в командах участников: %(1)s и %(2)s!' % {"1": team1_num, "2": team2_num})

print("Команда {} решила задач: {}!".format(time2_name, score_2))
print("{} решили задачи за {}с !".format(time2_name, team2_time))

print(f"Команды решили {score_1} и {score_2} задач.")
print(f"Результат битвы: {result}!")
print(f"Сегодня было решено {task_total} задач, в среднем по {time_avg} секунды на задачу!")
