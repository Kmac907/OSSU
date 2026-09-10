"""
4.10 Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
•	 Print the message The first three items in the list are:. Then use a slice to
print the first three items from that program’s list.
•	 Print the message Three items from the middle of the list are:. Use a slice to
print three items from the middle of the list.
•	 Print the message The last three items in the list are:. Use a slice to print the
last three items in the list.
"""

# 4_1.py
pizza = ["cheese", "pepperoni", "combo"]
"""
for i in pizza:
    print(f" I like {i}")
print("I love pizza!")

"""
# start 4_10.@py
print(pizza[:3])
three_from_middle = pizza[:1]
print(f"Three items from the middle of the list are:{three_from_middle}")
last_three_items = pizza[0:]
print(f"The last three items in the list are:{three_from_middle}")
