from string import ascii_uppercase

with open("names.txt", "r") as file:
    names = file.read()
    names = names.replace('"', "")
    names = names.split(",")

alphas = [char for char in ascii_uppercase]

names_worth = []
names.sort() # sort the names in alphabetical order 
for name in names:
    worth = 0
    for ch in name:
        worth += alphas.index(ch) + 1 # calculate worth based on the index of chars
    position = names.index(name) + 1 # position of the name in the sorted list
    names_worth.append(worth * position) # store their final value
print(sum(names_worth))