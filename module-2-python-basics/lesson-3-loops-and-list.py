"""
Module 2 — Lesson 3: Loops & Lists
Student: Pierce Darby Laxamana
Date: September 27, 2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
Imagine you have a playlist of 50 songs. A list is exactly that—a single 
collection that holds multiple items in a specific order so you don't have to 
create 50 different variables. 

A loop is how you interact with that list without losing your mind. Instead 
of writing "play song 1, play song 2, play song 3..." manually in your code, 
a loop lets you say, "Go through this entire list, and for every song you find, 
play it." Loops automate repetitive tasks, making your code clean and efficient.


============================================
KEY VOCABULARY
============================================
- list: A data structure that holds an ordered collection of items inside square 
  brackets `[]`. It can hold strings, numbers, or even other lists.
  
- for loop: A loop designed to run a specific number of times, usually by moving 
  through a sequence (like a list) item by item until it reaches the end.
  
- while loop: A loop that keeps running indefinitely as long as a specific 
  condition remains True. It only stops when that condition becomes False.
  
- index: The numerical position of an item inside a list. In Python, counting 
  starts at 0, not 1.
  
- iteration: One complete cycle or pass through the block of code inside a loop.


============================================
MY OWN EXAMPLE(S)
============================================
"""

# --- EASY FOR LOOP EXAMPLE ---
# A simple list of strings representing my favorite bands
favorite_bands = ["Modern Baseball", "American Football", "Mom Jeans", "Brakence"]

print("My Playlist:")
for band in favorite_bands:
    print(f"- Now playing: {band}")

print("\n") 


countdown = 3

print("Starting the show in...")

while countdown > 0:
    print(countdown)
    countdown -= 1  

print("Let's go!")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
The biggest mistake with `while` loops is creating an "infinite loop." If I 
forgot to include `countdown -= 1` in the example above, the variable would 
stay at 3 forever. The loop would just print "3" endlessly until my computer 
crashed or I forced the program to stop.

With lists, the most confusing part is that counting starts at 0. If I want 
to get "Modern Baseball" from my list, I have to ask for `favorite_bands[0]`, 
not `favorite_bands[1]`..


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
