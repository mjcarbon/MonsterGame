Maxim Joel Carbonell-Kiamtia
mjcarbon

---------------------
DESCRIPTION
MonsterGame is a program that allows user to create different types of monsters with different health levels and attacks.
User can then initiate fights between monsters and the program will build experience and level them up.

-----------
FILES
One.py
README.tx
-
One.py

This file is the python program to create monsters with different levels of health and attacks which gets implemented
when the program initiates its battle functionality.

Instructions to use "Lab1.lgi":
This file is to be run using any python interpreter.

The following commands is to create a monster with a name, attack, and health:
------------------------
bob = Dragon("bob", 18)
bob.add_attack("ice_storm")
bob.remove_attack("ice_storm")
------------------------
To use the fighting functionality with experience points use the following with two monsters already created i.e. "bob" and "jack":
------------------------
round1, winner, moves = monster_fight(bob, jack)
print(round1) -----> returns round at which monster won
print(winner.name) -----> returns name of which monster won
print(winner.attacks) ---------> returns name of attacks used and their damage points
print(winner.exp) ---------> returns experience level
print(winner.max_hp) ---------> returns max health level
print(moves) ---------> returns name of moves used to win
--------------------
Example Input:

a = Dragon("a", 18)
b = Ghost("b", 18)
a.add_attack("ice_storm")
b.add_attack("double_hit")
b.remove_attack("wait")
round1, winner, moves = monster_fight(a, b)
print(round1)
print(winner.name)
print(winner.attacks)
print(winner.exp)
print(winner.max_hp)
print(moves)
round1, winner, moves = monster_fight(a, b)
print(round1)
print(winner.name)
print(winner.attacks)
print(winner.exp)
print(winner.max_hp)
print(moves)
