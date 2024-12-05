worddic = {} #empty dictionary
sentence = input("give sentence\n") #asks user for sentence to use

sentence1 = sentence.split() #creates a new list from the string of the sentence split into seperate words

for x in range(len(sentence1)): #for loop that repeats for every word in the list
    sentence1[x] = sentence1[x].lower() #turns each word into lowercase 


for x in sentence1: #for loop 
    count = sentence1.count(x) #counts how many times each words appears
    worddic[x] = count #appends this into empty dictionary


for x in worddic: #for loop, amt of loops = amount of unique words in dictionary
    print(x,"|",worddic[x]) #prints the word as x, then the amount of times it appears
    
    
ync = input('would you like to see frequency of letters(y = yes, n = no)\n')    

characdic = {} #empty dictionary for letters and frequency 
if "y" in ync:
    for character in sentence.lower(): #for loop, amt of loops = amount of unique letters in sentence
        if character.islower() and character not in characdic:
            characdic[character] = sentence.count(character)

    
    
for x in characdic:
    print(x,"|",characdic[x])
        
    





'''if char in sentence:
    for letter in abc:
        count = sentence.count(letter)
        characdic[letter] = count

for x in characdic:
    print(x,'|',characdic[x])'''

    


















'''
cchc = input("enter a character:	")
cchc = str(cchc)
if cchc in sentence:
    count = sentence.count(cchc)
    characdic[cchc] = count
    print(characdic)
else:
    print('character not in sentence')
'''
    
    
    




    
    
    
    
