#-----------------------------------------------------------------------------
# Name:        Introduction (main.py)
# Purpose:     
#
# Author:      Mr. Kowalczewski
# Created:     14-Aug-2018
# Updated:     14-Aug-2018
#-----------------------------------------------------------------------------



item_costs = {"apples": 2.50, "bananas": 1.75, "milk": 3.00}
item_list = ["apples", "bananas", "milk"]

#1
item_name = input("Which item price do you want to check? ")
print(f"The price of {item_name} is ${item_costs[item_name]}")


#2
budget = 10.00
num_people = input("How many people are sharing the cost? ")
cost_per_person = budget / int(num_people)
print(f"That will be ${cost_per_person:.2f} per person.")

#3
print("Checking the 6th item on your list...")
item = item_list[5]
print(f"The 6th item is {item}.")

#4
message = "You have " + len(item_list) + " items on your list."
print(message)


#5
print(final_greeting)
