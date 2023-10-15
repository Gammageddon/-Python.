list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
count = len(list_players)
count_in_team = int(count / 2)
# TODO Разделите участников на две команды
print(list_players[:count_in_team])
print(list_players[count_in_team:])
