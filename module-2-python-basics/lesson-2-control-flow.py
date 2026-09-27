"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: Pierce Darby Laxamana
Date: September 27, 2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
Control flow is how a program makes decisions. Without it, a script just reads 
top to bottom and does the exact same thing every time. so whenever Control flow acts like 
a fork in the road. It lets the program look at the current situation—like user 
input, a sensor reading, or a character's health—and decide which chunk of 
code to run next. It’s basically the logic of cause and effect in programming.


============================================
KEY VOCABULARY
============================================
- condition: A specific test the program runs that can only result in a True 
  or False answer.
- if / elif / else: The keywords used to build the decision branches. `if` checks 
  the first condition. elifchecks alternate conditions if the first 
  one fails. else is the default fallback that runs if absolutely nothing 
  above it was True.
- comparison operator: Symbols used to compare values, like `==` (is equal to), 
  `!=`, < and >
- boolean expression: Any mathematical or logical statement that ultimately 
  boils down to a single True or False state when the computer evaluates it.


============================================
MY OWN EXAMPLE(S)
============================================
"""
player_hp = 30
enemy_damage = 45
has_revive_item = True
player_action = "defend"

print(f"Enemy attacks for {enemy_damage} damage!")

if player_action == "defend":
    damage_taken = enemy_damage / 2
    player_hp -= damage_taken
    print(f"You raised your shield! Took {damage_taken} damage. HP left: {player_hp}")

elif player_hp > enemy_damage:
    player_hp -= enemy_damage
    print(f"You took the hit! HP left: {player_hp}")

elif has_revive_item:
    player_hp = 100
    has_revive_item = False
    print("Revived")

else:
    player_hp = 0
    print("You have been defeated...")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
The absolute classic mistake is using a single equals signinstead of a 
double equals sign in an if statement. I've done this so many times. 
x = 5 assigns the value 5 to x, whereas x == 5 asks is x equal to 5?. 
If you mix them up, Python throws a syntax error.

Another frustrating one is indentation errors. Python uses spaces/tabs to know 
which code belongs inside the `if` block. If your indentation is off by even 
one space, the program either breaks or runs the logic out of order.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
