# Question 16(b)
# Examination Number:230520
import random as r
def randnum(maximum):
    maxint = int(maximum)
    thirty = maxint * 0.3
    twenty = maxint * 0.2
    difference = 0
    userguess = 0
    score = 0
    
    running = True
    while running:
        secret = r.randint(1,maxint)
        userguess = int(input("Enter your guess: "))
        
            
        if userguess > secret:
            difference = userguess - secret
            if difference <=twenty:
                score += 20
                print(f'Secret number is {secret}. You guessed {userguess}. Difference is {difference}.')
                print('You score 20 points!')
                print(f'Score = {score}')
                
            elif difference >= thirty:
                score-=30
                print(f'Secret number is {secret}. You guessed {userguess}. Difference is {difference}.')
                print('You lose 30 points.')
                print(f'Score = {score}')
            else:
                print(f'Secret number is {secret}. You guessed {userguess}. Difference is {difference}.')
                print(f'Score = {score}')
        if userguess < secret:
            difference = secret - userguess
            if difference <= twenty:
                score += 20
                print(f'Secret number is {secret}. You guessed {userguess}. Difference is {difference}.')
                print('You score 20 points!')
                print(f'Score = {score}')
                
            elif difference >= thirty:
                score-=30
                print(f'Secret number is {secret}. You guessed {userguess}. Difference is {difference}.')
                print('You lose 30 points.')
                print(f'Score = {score}')
            else:
                print(f'Secret number is {secret}. You guessed {userguess}. Difference is {difference}.')
                print(f'Score = {score}')
            
        if userguess == secret:
            print("Jackpot! You score 100 points!")
            score+=100
            print(f'Score = {score}')
        cont = input('Continue? y/n: ')
        if cont != 'y':
            running = False
            print(f'Final score = {score}')
        
randnum(100)