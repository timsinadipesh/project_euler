"""
1. reads a text file containing over 5k first names
2. sorts them into alphabetical order
3. finds the worth of names based on the index of their characters
4. finds the position of name in sorted list
5. derives the final value with the name worth and position
6. prints the total value of all the names
"""

from string import ascii_uppercase

with open("names.txt", "r") as file:
    names = file.read() 
    names = names.replace('"', "")
    names = names.split(",")

alphas = [char for char in ascii_uppercase]

names_worth = []
names.sort() 
for name in names:
    worth = 0
    for ch in name:
        worth += alphas.index(ch) + 1 
    position = names.index(name) + 1 
    names_worth.append(worth * position)
print(sum(names_worth))