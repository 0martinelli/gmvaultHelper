import os

f = open('users.txt','r')

lines = f.readlines()

for c in range(0,len(lines)):

    index = lines[c].find('@')

    nome = lines[c]

    lines[c] = nome[:index]

print(lines)

for c in range(0,len(lines)):
    os.mkdir('/Users/jeferson.martinelli/Desktop/'+lines[c])
