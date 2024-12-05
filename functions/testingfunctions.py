choosing2 = True

f=open('Passwords.csv','r')
header = f.readline()
data1 = []
for line in f:
    data1.append(line.split(', '))

a=open('Passwords.csv','a')
while choosing2:
    newuser = input('Enter a new User ID: ')
    if newuser in [user[0] for user in data1]: #list comprehension to get list of users from list of users and passwords(data) 
        print('User ID already exists, Try again.')

    else:
        choosing2 = False
choosing3 = True
print('''Your password should have at least 8 characters
It should include upper case letters
It should include lower case letters
It should include numbers
It should include one special character !, £, $, €, %, &, *, #
''')
while choosing3:    
    passw = input('Enter a valid password: ')
    if validpassword(passw):
        choosing3 = False
                     
a.write('\n'+newuser+', '+passw)
a.close()
