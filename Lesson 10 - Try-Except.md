# Lesson 10 - Try/Except

The example code for this lesson is in `try_except.py`. Open it alongside these
notes and run it as we go.

We have run into several kinds of errors so far:

```python
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
```

Remove the `#` from one line at a time and run it to see each error. There are
more types of errors, but these are the most common for us.

How can we stop our programs from crashing when these errors happen?

## try/except

Python can **try** to run code, as long as we give it a backup plan with
**except**:

```python
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
```

Now the program doesn't crash.

## Several excepts

A try block can hold as much code as you like, with a separate except for each
type of error that code might cause:

```python
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
```

After the first error, the code jumps to the matching except and skips the rest
of the try block. Ideally a try block does not hold a lot of unrelated code
(more on that below).

## else

An `else` after the last except runs only if everything in the try block
succeeded.

## Converting input()

`input()` always gives back a string, even when the user types digits. To do
math with it we convert it with `int()`:

```python
age = int(input("How old are you? "))
print(f"Next year you will be {age + 1}.")
```

Run this and type `15`. It works. Now run it again and type `fifteen`:

```
How old are you? fifteen
Traceback (most recent call last):
  File "try_except.py", line 107, in <module>
    age = int(input("How old are you? "))
ValueError: invalid literal for int() with base 10: 'fifteen'
```

`int()` was given a string, which is the correct type, but the value inside it
is not a whole number. That makes it a **ValueError**. `15.5` and an empty
entry (just pressing Enter) cause the same error.

We cannot control what the user types, so any `int(input())` can crash. Wrap it
in try/except:

```python
try:
    age = int(input("How old are you? "))
except ValueError:
    print("That is not a whole number.")
else:
    print(f"Next year you will be {age + 1}.")
```

The `print` goes in `else`, not after the try/except. If the conversion fails,
`age` never gets a value, so using it afterwards would cause a NameError.

## Best practices

1. Keep each try block short. Include only code that might cause an error, or
   code that must be skipped if an error happens.
2. Give specific error messages. A bare `except:` catches every error, but then
   neither you nor the user knows what went wrong.

## Lab

That is it for the lesson. Move on to Lab 10, in `README.md`.
