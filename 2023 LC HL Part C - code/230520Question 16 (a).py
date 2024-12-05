# Question 16(a)
# Examination Number: 230520
from random import randint

def guess_game(max_guesses_allowed):
    secret_number = randint(1, 5)
    guess_count = 0
    user_guess = 0
    guesslist = []

    while (user_guess != secret_number):
        user_guess = int(input("Enter your guess: "))
        if user_guess not in guesslist:
            guesslist.append(user_guess)
            guess_count += 1 #Increase guess_count by 1
        else:
            print(f'You already guessed {user_guess}, try again.')
        if guess_count == max_guesses_allowed:
            print('You ran out of guesses. You lose.')
            break
        elif user_guess > secret_number:
            print('Sorry! Your guess was too high.')
        elif user_guess < secret_number:
            print('Sorry! Your guess was too low.')
        elif user_guess == secret_number:
            print("Congratulations! You win!")
            if guess_count == 1:
                print(f'You took {guess_count} guess')
            else:
                print(f'You took {guess_count} guesses')

def guess_gameH(max_guesses_allowed):
    secret_number = randint(1, 100)
    guess_count = 0
    user_guess = 0
    guesslist = []

    while (user_guess != secret_number):
        user_guess = int(input("Enter your guess: "))
        if user_guess not in guesslist:
            guesslist.append(user_guess)
            guess_count += 1 #Increase guess_count by 1
        else:
            print(f'You already guessed {user_guess}, try again.')
        
        if user_guess == secret_number:
            print("Congratulations! You win!")
            if guess_count == 1:
                print(f'You took {guess_count} guess')
            else:
                print(f'You took {guess_count} guesses')
        elif guess_count == max_guesses_allowed:
            print('You ran out of guesses. You lose.')
            break
        elif user_guess > secret_number:
            print('Sorry! Your guess was too high.')
        elif user_guess < secret_number:
            print('Sorry! Your guess was too low.')
        

print("Welcome to the guessing game!")
maxg = int(input('Enter max number of guesses: '))
difficulty = input('Enter difficulty e(asy) or h(ard): ')
if 'h' in difficulty:
    guess_gameH(maxg)
else:
    guess_game(maxg)
