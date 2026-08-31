"""
4-8. Cubes: A number raised to the third power is called a cube. For example,
the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
is, the cube of each intege).
"""
num = list(range(1,11))
solution = list()
for i in num:
    cube = i**3
    #print(cube)
    solution.append(cube)
print(solution)
