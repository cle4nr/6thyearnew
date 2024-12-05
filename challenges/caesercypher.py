riddle = input('enter a string: ')
from string import ascii_lowercase
for x in riddle:
    if x.isalpha():
        i = ascii_lowercase.find(x)
        i = (i + 2) % 26
        letter = ascii_lowercase[i]
        print(letter,end='')
    else:
        print(x,end = '')
