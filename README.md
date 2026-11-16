# Lab 10 - Fixing Errors

`main.py` already contains a short program with five numbered blocks (`#1` to
`#5`). Each block can crash. Your job is to stop the crashes with try/except.

Do **not** delete or change any of the existing code. Wrap it in try/except
instead.

Open `main.py` and complete the following:

1. Update the header with your information (Name, Purpose, Author, Created, Updated).
2. Run the program and try different inputs to find which error each block causes.
3. Give each block its own try/except. Name the error in every except (for example `except KeyError:`), never a bare `except:`.
4. Block #1: if the item is not in `item_costs`, print `Sorry, '____' is not on the price list.` with the item name in the blank (keep the single quotes).
5. Block #2: if the number of people is not a number, print `Invalid Number`
6. Block #3: if there is no 6th item, print `There is no 6th item`
7. Block #4: in the except, print the message the code was trying to build, with the correct number of items: `You have 3 items on your list.` (use `len(item_list)`, do not type the 3).
8. Block #5: `final_greeting` does not exist. In the except, print `Goodbye!`

The two prompts are already in the code: `Which item price do you want to check? `
and `How many people are sharing the cost? `. Assume the number of people is
never 0.

## Running your program

Open `main.py` and press the Run button in the top right corner of VS Code. Your output appears in the terminal at the bottom.

## Checking your work

Press **Ctrl+Shift+B** to run the tests. You will see one line per test:

```
[PASS] 1. Header is filled in
[FAIL] 2. Item found, valid number
```

When a test fails it shows what was expected and what your program printed. Fix your code and press Ctrl+Shift+B again. Keep going until all tests pass.

## Reminders

- Fill in every field of the header before you write any code.
- Write comments as you go. Say which error each except is catching and why it happens.
- Tests check your output exactly. Copy each message exactly, including capitals and punctuation.
- Keep each try block short: only the lines that can fail, and the lines that should be skipped when they do.

## Optional challenges

Finished early? Try the optional challenges in the `challenges` folder. Open `challenges/CHALLENGES.md` for instructions. They are not assessed and do not affect your lab result.
