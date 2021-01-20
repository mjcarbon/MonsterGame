from Fight import monster_fight
from Sorter import most_occurences,sort_dict,sort_dict_over4

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

