# Optional Challenges - Lab 10

**These challenges are optional.** Try them once Lab 10 passes every test. They are
not assessed, and they do not affect your lab result.

| File | Challenge |
|---|---|
| `try_except_challenge.py` | Crash-Proof Program |
| `safe_divide.py` | Safe Divide |
| `total_values.py` | Total the Values (harder) |

## Crash-Proof Program

1. Open your Lab 9 `main.py` and copy all of your code (not the header) into
   `try_except_challenge.py`, just below the header.
2. Add `try` and `except` so that your program never crashes, whatever the user
   types. Test it by typing words where it expects a number.

This challenge is open-ended. The tests only check that your code uses `try` and
`except`, and that it has comments. Run your program yourself and try to break it.

## Safe Divide

Open `safe_divide.py` and complete `safe_divide(a, b)`. It divides `a` by `b`
and **returns** (does not print) a message:

1. If the division works, return the question and the answer to 2 decimal places:
   `safe_divide(12, 4)` returns `"12 / 4 = 3.00"`
2. Dividing by zero raises a `ZeroDivisionError`. Catch it and return
   `Error: Cannot divide by zero.`
3. Dividing text raises a `TypeError`. Catch it and return
   `Error: Both values must be numbers.`

Name the error in each except. No bare `except:`.

`ZeroDivisionError` was not in the lesson. Run `print(5 / 0)` on its own to see it.

## Total the Values (harder)

Open `total_values.py` and complete `total_values(values)`. `values` is a list.
Most items are numbers stored as text, like `"3.5"`, but some are not.

1. Loop through the list and add up every item that `float()` can convert.
2. Skip anything `float()` cannot convert, and count how many you skipped. A word
   like `"two"` raises a `ValueError`. `None` raises a `TypeError`.
3. Return `Total: ____ (__ skipped)` with the total to 2 decimal places.

For example, `total_values(["4", "two", "3.5", "7"])` returns
`"Total: 14.50 (1 skipped)"`, and an empty list returns `"Total: 0.00 (0 skipped)"`.

Put the try/except **inside** the loop, so one bad item does not stop the rest
from being added.

Do not rename any `def` line. The tests call the functions by name.

## Running your program

Open the challenge file and press the Run button in the top right corner of VS
Code. Your output appears in the terminal at the bottom.

## Checking your work

Press **Ctrl+Shift+B**, the same as for the lab. The Lab 10 results appear first.
Scroll down to the **OPTIONAL CHALLENGES** section for these.

`SKIP` means you have not started that challenge yet. It is not an error.

## Reminders

- These are optional. Finish Lab 10 first.
- Keep each try block short: only the lines that can fail.
- Say in a comment which error each except catches.
- Returned text is matched exactly, including `Error: ` and the period.
