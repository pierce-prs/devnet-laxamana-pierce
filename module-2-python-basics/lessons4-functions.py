"""
Module 2 — Lesson 4: Functions
Student: Laxamana, Pierce Darby A.
Date: September 27, 2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
A function is like a reusable block of code that performs a specific task.
so Instead of writing the same code many times, 
we can put it inside a function and call the function whenever we need it.
A function can receive information through parameters 
and can return a result after doing its task.

============================================
KEY VOCABULARY
============================================
- function: a reusable block of code that performs a specific task. 
- def: the keyword used to define a function in Python.
- parameter: a variable that receives a value inside a function. 
- argument: the actual value passed to a parameter when the function is called. 
- return value: the result that a function sends back to the code that called it. 
- function call: using the function so that its code runs.


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

def calculate_total(price, quantity):
    return price * quantity
    item_total = calculate_total(50, 3) 
    
    print("Total:", item_total)


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
One mistake I want to avoid is confusing a parameter with an argument.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""