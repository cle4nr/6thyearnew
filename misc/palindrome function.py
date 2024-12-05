def palindromecheck(word):
    if word == word[::-1]:
        return True
    else:
        return False
        
word = input('enter a word to check for palindrome: ')
print(f'{word} is a palindrome: {palindromecheck(word)}')

