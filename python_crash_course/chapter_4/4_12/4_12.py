"""
4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing to save space. Choose a version of foods.py, and write two for loops to print each list of foods.
"""

my_foods = ['pizza', 'falafel', 'carrot cake']
# This doesn't work:
friend_foods = my_foods
print("My favorite foods are:")
for i in my_foods:
    print(i)
print("\nMy friend's favorite foods are:")   
for f in friend_foods:
    print(f) 
