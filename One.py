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


class Monster():
    def __init__(self, name, max_hp=20, type="normal"):
        self.name = name
        self.type = type
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.exp = 0
        self.attacks = {"wait": 0}
        self.possible_attacks = {"sneak_attack": 1, "slash": 2, "ice_storm": 3, "fire_storm": 3, "whirlwind": 3,
                                 "earthquake": 2, "double_hit": 4, "wait": 0}

    def add_attack(self, attack_name):
        if not attack_name in self.possible_attacks:
            return False
        if attack_name in self.attacks:
            return False
        if len(self.attacks) >= 4:
            lowest_index = len(self.attacks) - 1
            sortedAttacks = sort_dict_over4(self.attacks)
            lowest_attack = sortedAttacks[lowest_index][0]
            self.attacks.pop(lowest_attack)
        if len(self.attacks) < 4:
            if attack_name in self.possible_attacks:
                if attack_name == "sneak_attack":
                    self.attacks["sneak_attack"] = 1
                    return True
                elif attack_name == "slash":
                    self.attacks["slash"] = 2
                    return True
                elif attack_name == "ice_storm":
                    self.attacks["ice_storm"] = 3
                    return True
                elif attack_name == "fire_storm":
                    self.attacks["fire_storm"] = 3
                    return True
                elif attack_name == "whirlwind":
                    self.attacks["whirlwind"] = 3
                    return True
                elif attack_name == "earthquake":
                    self.attacks["earthquake"] = 2
                    return True
                elif attack_name == "double_hit":
                    self.attacks["double_hit"] = 4
                    return True
                elif attack_name == "wait":
                    self.attacks["wait"] = 0
                    return True
            else:
                return False

    def remove_attack(self, attack_name):
        if not attack_name in self.possible_attacks:
            return False
        if attack_name in self.attacks:
            self.attacks.pop(attack_name)
            if len(self.attacks) == 0:
                self.attacks["wait"] = 0
            return True

    def win_fight(self):
        self.exp += 5
        self.current_hp = self.max_hp

    def lose_fight(self):
        self.exp += 1
        self.current_hp = self.max_hp


class Dragon():
    def __init__(self, name, max_hp=20):
        self.name = name
        self.type = "dragon"
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.exp = 0
        self.attacks = {"wait": 0}
        self.possible_attacks = {"sneak_attack": 1, "slash": 2, "ice_storm": 3, "fire_storm": 3, "whirlwind": 3,
                                 "earthquake": 2, "double_hit": 4, "wait": 0}
        self.increment = 0

    def add_attack(self, attack_name):
        if not attack_name in self.possible_attacks:
            return False
        if attack_name in self.attacks:
            return False
        if len(self.attacks) >= 4:
            lowest_index = len(self.attacks) - 1
            sortedAttacks = sort_dict_over4(self.attacks)
            lowest_attack = sortedAttacks[lowest_index][0]
            self.attacks.pop(lowest_attack)
        if len(self.attacks) < 4:
            if attack_name in self.possible_attacks:
                if attack_name == "sneak_attack":
                    self.attacks["sneak_attack"] = 1
                    return True
                elif attack_name == "slash":
                    self.attacks["slash"] = 2
                    return True
                elif attack_name == "ice_storm":
                    self.attacks["ice_storm"] = 3
                    return True
                elif attack_name == "fire_storm":
                    self.attacks["fire_storm"] = 3
                    return True
                elif attack_name == "whirlwind":
                    self.attacks["whirlwind"] = 3
                    return True
                elif attack_name == "earthquake":
                    self.attacks["earthquake"] = 2
                    return True
                elif attack_name == "double_hit":
                    self.attacks["double_hit"] = 4
                    return True
                elif attack_name == "wait":
                    self.attacks["wait"] = 0
                    return True
            else:
                return False

    def remove_attack(self, attack_name):
        if not attack_name in self.possible_attacks:
            return False
        if attack_name in self.attacks:
            self.attacks.pop(attack_name)
            if len(self.attacks) == 0:
                self.attacks["wait"] = 0
            return True

    def win_fight(self):
        self.exp += 5
        self.current_hp = self.max_hp
        self.increment += 5
        if self.increment >= 10:
            for attack in self.attacks:
                self.attacks[attack] += 1
            self.increment = 0

    def lose_fight(self):
        self.exp += 1
        self.current_hp = self.max_hp
        self.increment += 1
        if self.increment >= 10:
            for attack in self.attacks:
                self.attacks[attack] += 1
            self.increment = 0


class Ghost():
    def __init__(self, name, max_hp=20):
        self.name = name
        self.type = "ghost"
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.exp = 0
        self.attacks = {"wait": 0}
        self.possible_attacks = {"sneak_attack": 1, "slash": 2, "ice_storm": 3, "fire_storm": 3, "whirlwind": 3,
                                 "earthquake": 2, "double_hit": 4, "wait": 0}
        self.increment = 0

    def add_attack(self, attack_name):
        if not attack_name in self.possible_attacks:
            return False
        if attack_name in self.attacks:
            return False
        if len(self.attacks) >= 4:
            lowest_index = len(self.attacks) - 1
            sortedAttacks = sort_dict_over4(self.attacks)
            lowest_attack = sortedAttacks[lowest_index][0]
            self.attacks.pop(lowest_attack)
        if len(self.attacks) < 4:
            if attack_name in self.possible_attacks:
                if attack_name == "sneak_attack":
                    self.attacks["sneak_attack"] = 1
                    return True
                elif attack_name == "slash":
                    self.attacks["slash"] = 2
                    return True
                elif attack_name == "ice_storm":
                    self.attacks["ice_storm"] = 3
                    return True
                elif attack_name == "fire_storm":
                    self.attacks["fire_storm"] = 3
                    return True
                elif attack_name == "whirlwind":
                    self.attacks["whirlwind"] = 3
                    return True
                elif attack_name == "earthquake":
                    self.attacks["earthquake"] = 2
                    return True
                elif attack_name == "double_hit":
                    self.attacks["double_hit"] = 4
                    return True
                elif attack_name == "wait":
                    self.attacks["wait"] = 0
                    return True
            else:
                return False

    def remove_attack(self, attack_name):
        if not attack_name in self.possible_attacks:
            return False
        if attack_name in self.attacks:
            self.attacks.pop(attack_name)
            if len(self.attacks) == 0:
                self.attacks["wait"] = 0
            return True

    def win_fight(self):
        self.exp += 5
        self.current_hp = self.max_hp
        self.increment += 5
        if self.increment >= 10:
            self.max_hp += 5
            self.increment = 0

    def lose_fight(self):
        self.exp += 1
        self.current_hp = self.max_hp
        self.increment += 1
        if self.increment >= 10:
            self.max_hp += 5
            self.increment = 0


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


