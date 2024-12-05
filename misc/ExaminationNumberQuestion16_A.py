# Question 16(a)
# Examination Number:
import random as r


fruits = ['apple', 'cherry', 'orange']
fruit_1, fruit_2, fruit_3 = r.choice(fruits), r.choice(fruits), r.choice(fruits)
print('Random Fruit 1:',fruit_1)
print('Random Fruit 2:',fruit_2)
print('Random Fruit 3:',fruit_3)

if fruit_1 == fruits[1]:
    print('First fruit is cherry.')

if fruit_1 == fruit_2 or fruit_2 == fruit_3 or fruit_1 == fruit_3:
    print('Matching pair.')
    if fruit_1 == fruit_2:
        print('First pair match.')
    if fruit_1 == fruits[1]:
        print('First pair are cherries.')
        
        
appleamt = 0
cherryamt = 0
orangeamt = 0
for x in range(100):
    fruit = r.choice(fruits)
    if fruit == fruits[0]:
        appleamt += 1
    if fruit == fruits[1]:
        cherryamt += 1
    if fruit == fruits[2]:
        orangeamt += 1
print()



print('apples',appleamt)
print('cherries',cherryamt)
print('oranges',orangeamt)
print()

fruits1 = ['apple', 'cherry', 'orange']
print('initial list of fruits:\n',fruits1)
newfruit = input('enter a new fruit: ')
fruits1.append(newfruit)
print('new list of fruits:\n',fruits1)
choosewin = True
while choosewin:
    print('enter your winning fruit in list',fruits1)
    winfruit = input()
    if winfruit in fruits1:
        choosewin = False
        print('The winning fruit you selected is',winfruit)
    else:
        print('fruit not in list')
running = True
tries = 0
while running:
    tries += 1
    a = r.choice(fruits1)
    b = r.choice(fruits1)
    c = r.choice(fruits1)
    if a == b == c == winfruit:
        print('Winner after',tries,'tries')
        running = False
        

