
def find_common_participants(first, second, razd = ","):
    group_1 = set(first.split(razd))
    group_2 = set(second.split(razd))
    obsh = list(group_1.intersection(group_2))
    obsh.sort()

    return obsh

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, "|"))
