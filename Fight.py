def most_occurences(list):
    return max(set(list), key=list.count)


def sort_dict(dict):
    x = sorted(dict.items(), key=lambda i: i[1], reverse=True)
    last_index = len(x) - 1
    num_list = []
    for i in range(len(x)):
        num_list.append(x[i][1])
    common_num = most_occurences(num_list)
    most_times = num_list.count(common_num)

    count = 0
    while count < most_times:
        for i in range(len(x)):
            if i == last_index:
                break
            if x[i][1] == x[i + 1][1]:
                if x[i][0] > x[i + 1][0]:
                    (x[i], x[i + 1]) = (x[i + 1], x[i])
        count += 1

    return x


def sort_dict_over4(dict):
    x = sorted(dict.items(), key=lambda i: i[1], reverse=True)
    last_index = len(x) - 1
    num_list = []
    for i in range(len(x)):
        num_list.append(x[i][1])
    common_num = most_occurences(num_list)
    most_times = num_list.count(common_num)

    count = 0
    while count < most_times:
        for i in range(len(x)):
            if i == last_index:
                break
            if x[i][1] == x[i + 1][1]:
                if x[i][0] < x[i + 1][0]:
                    (x[i], x[i + 1]) = (x[i + 1], x[i])
        count += 1

    return x

def monster_fight(monster1, monster2):
    round = 0
    moves1 = []
    moves2 = []
    monster1_sorted = sort_dict(monster1.attacks)
    monster2_sorted = sort_dict(monster2.attacks)
    turn1 = True
    if monster1_sorted[0][0] == "wait" and monster2_sorted[0][0] == "wait":
        return (-1, None, None)
    index1 = 0
    index2 = 0
    while monster1.current_hp > 0 or monster2.current_hp > 0:
        if turn1 == True:
            if index1 == len(monster1_sorted):
                index1 = 0
            monster2.current_hp -= monster1_sorted[index1][1]
            moves1.append(monster1_sorted[index1][0])
            index1 += 1
            round += 1
            if monster2.current_hp <= 0:
                monster1.win_fight()
                monster2.lose_fight()
                return (round, monster1, moves1)
            turn1 = False
        else:
            if index2 == len(monster2_sorted):
                index2 = 0
            monster1.current_hp -= monster2_sorted[index2][1]
            moves2.append(monster2_sorted[index2][0])
            index2 += 1
            turn1 = True
            if monster1.current_hp <= 0:
                monster2.win_fight()
                monster1.lose_fight()
                return (round, monster2, moves2)


