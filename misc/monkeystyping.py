import random
targetWord = "T"

def monkeystyping():
    guessNumber = random.randint(65,90)
    letter1 = chr(guessNumber)
    count = 1
    guess = letter1
    print(guess)
    
    while guess != targetWord:
        guessNumber = random.randint(65,90)
        letter1 = chr(guessNumber)
        guess = letter1
        print(guess)
        count+=1
    return count

avg = []
for x in range(3):
    a = monkeystyping()
    avg.append(a)
    print(a)
sumlist = sum(avg)
avgofavglist = sumlist / len(avg)
print(avg)
print(f"Average of 3 runs: {avgofavglist:.1f}")
    