#1
def firstlet(word):
    return word[0]

words = ['apple','banana','cherry']
firstletters = list(map(firstlet,words))
print(firstletters)
#2
def makeupper(word):
    return word.upper()
upperlist = list(map(makeupper,words))
print(upperlist)

#3
s = [' hello ', '  world ', '  python ']
def removewhite(string):
    return string.strip(' ')
            
nowhite = list(map(removewhite,s))
print(nowhite)

#4
celcius = [0,20,-40,100,-32]
def c_to_f(cel):
    return cel*(9/5)+32
fahr = list(map(c_to_f, celcius))
print(fahr)
            