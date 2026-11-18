#-----------------------------------------------------------------------------
# Name:        Try/Except (try_except.py)
# Purpose:     Demonstrating common errors and handling them with try, except,
#              else and finally, including converting input() to an int
#
# Author:      Mr. Kowalczewski
# Created:     28-Sept-2026
# Updated:     18-Nov-2026
#-----------------------------------------------------------------------------

# --- Common errors (remove one # at a time to see each crash) ----------------
my_list = [0, 8, 12]
my_dict = {'a': 10, 'z': 18}

# NameError (variable doesn't exist)
#print(student_name)

# ValueError (correct type, wrong value)
# int() does take a string, so this is NOT a TypeError
#age = int("123asfsdf")
#weight = int(input("What is your weight in lbs? "))

# TypeError (incorrect type)
#age = 12 + "abc"
#print(my_list[1.2])

# IndexError (index value doesn't exist)
#print(my_list[8])

# KeyError (key doesn't exist)
#print(my_dict['c'])


# --- try/except --------------------------------------------------------------
# NameError (variable doesn't exist)
try:
    print(student_name)
except:
    print("Variable doesn't exist")

# ValueError (correct type, wrong value)
try:
    age = int("123abc")
except:
    print("Can't convert this to integer")

# TypeError (incorrect type)
try:
    age = 12 + "abc"
except:
    print("Can't add these two things")

# IndexError (index value doesn't exist)
my_list = [0, 8, 12]
try:
    print(my_list[8])
except:
    print("Index 8 doesn't exist")

# KeyError (key doesn't exist)
my_dict = {'a': 10, 'z': 18}
try:
    print(my_dict['c'])
except:
    print("Key 'c' doesn't exist")


# --- Several excepts, else and finally ---------------------------------------
my_list = [0, 8, 12]
my_dict = {'a': 10, 'z': 18}

# the try block stops as soon as ONE error occurs
try:
    print("try block is starting")
    #print(name)
    age = int("123abc")
    age = 12 + "abc"
    print("Does this run?")
    print(my_list[8])
    print(my_dict['c'])
except NameError:
    print("NameError: Variable doesn't exist")
except ValueError:
    print("Can't convert this to integer")
except TypeError:
    print("Can't add these two things")
except IndexError:
    print("Index 8 doesn't exist")
except KeyError:
    print("Key 'c' doesn't exist")
# a final 'except' catches any remaining unknown errors
except:
    print("Something else went wrong")
# else runs only if ALL the code in try succeeded
else:
    print("All is good")
# finally runs after try or except, either way
finally:
    print("What does this do?")


# --- Converting input() to an int -------------------------------------------
# input() always returns a string. int() raises a ValueError if that string is
# not a whole number (try: 15, fifteen, 15.5, or just pressing Enter).

# Without try/except: uncomment, run, and type "fifteen" to see the crash
#age = int(input("How old are you? "))
#print(f"Next year you will be {age + 1}.")

# With try/except: the program keeps running
try:
    age = int(input("How old are you? "))
except ValueError:
    print("That is not a whole number.")
# age only exists if the conversion worked, so use it in else
else:
    print(f"Next year you will be {age + 1}.")
