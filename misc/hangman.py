import random as r
wordlist = ['box','paper'] #double letters not accounted for
word = r.choice(wordlist)
wordtuple = tuple(word)
wordll = list(wordtuple)
sortedwt = sorted(wordll)
correctletters = []
falseletters = []
wordnotguessed = True
lives = 5
while wordnotguessed:
    letterw = input('enter a letter: ')
    if not letterw in word:
        falseletters.append(letterw)
        lives -= 1
        print(f'{letterw} not in word, you have {lives} lives left')
        if lives == 0:
            print(f'you lose, the word was {word}')
            wordnotguessed = False
    else:
        correctletters.append(letterw)
        print(f'{letterw} is in word')
        correctst = sorted(correctletters)
        if correctst == sortedwt:
            wordnotguessed = False
            print(f'you win, the word was {word}')
    
   
   
   
   

    
    
