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