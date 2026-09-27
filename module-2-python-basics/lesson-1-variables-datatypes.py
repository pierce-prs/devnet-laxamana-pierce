"""
Module 2 — Lesson 1: Variables & Data Types
Student: Laxamana, Pierce Darby A.
Date: September 27, 2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
For you.. Think of variables as labeled storage boxes. When you're building a script or 
an app, you need places to store information in the computer's memory so you 
can use it or change it later. You grab a box, write a descriptive name on it 
and put something inside.

Data Types are just the categories of what you're putting inside those boxes. 
Python needs to know what kind of data it is dealing with so it knows what 
rules apply. For instance, you can do math with numbers, but if you try to 
multiply two words together, then the program will break. 


============================================
KEY VOCABULARY
============================================
- variable: A named storage container in memory where we keep data that our 
  program needs to process.
- data type: The classification of the data, which dictates what operations 
  can be performed on it.
- int: Short for integer. A whole number without a decimal point (e.g., 42). 
  Used for counting discrete things.
- float: A number with a decimal point (e.g., 3.14). Used for precise 
  measurements or fractional values.
- string: Text data. It's always wrapped in quotes (single or double). Think 
  of it as a literal string of characters linked together.
- boolean: A simple True or False switch. Commonly used in conditional logic 
  to track states (like checking if a device is connected).


============================================
MY OWN EXAMPLE(S)
============================================
"""

sensor_location = "Library 2nd Floor"
decibel_reading = 45.2                
warning_threshold = 75              
is_monitoring = True                  

print(f"Location: {sensor_location}")
print(f"Current Noise Level: {decibel_reading} dB")
print(f"Monitoring Active: {is_monitoring}")

decibel_reading = 78.5
print(f"\n[ALERT] New reading at {sensor_location}: {decibel_reading} dB!")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
A classic mistake is forgetting that strings and numbers don't mix automatically 
when you try to combine them. If I try to do `print("The reading is " + decibel_reading)`, 
Python throws a `TypeError`. You have to cast the number to a string first using 
`str(decibel_reading)`, or just use f-strings (like I did in the example above), 
which automatically handles the conversion and is much easier to read.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
This connects directly to database design. When I was setting up tables in MySQL 
for web portals, I had to strictly define if a column was going to hold a `VARCHAR` 
(string), `INT` (integer), or `TINYINT` (boolean). Python variables are dealing with 
the exact same underlying memory concepts, except Python is dynamically typed—meaning 
it figures out the type on the fly when you assign the value, rather than forcing 
you to declare it beforehand like SQL or C++ does.
"""
