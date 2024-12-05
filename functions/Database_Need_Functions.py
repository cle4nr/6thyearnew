#overwriting password
def validpassword(passw):
    if len(passw) < 8:
            print('Too short, needs atleast 8 characters.')
            return False
    else:
        hasupper = haslower = hasnumber = hasspecial = False
        for c in passw:
            if c.isupper():
                hasupper = True
            elif c.islower():
                haslower = True
            elif c.isdigit():
                hasnumber = True
            elif not c.isalnum():
                hasspecial = True
        if all((hasupper,haslower,hasnumber,hasspecial)): #if hasupper and haslower and hasnumber and hasspecial: 
            return True
            
        else:
            if not hasupper:
                print('No uppercase letters, needs atleast 1.')
            if not haslower:
                print('No lowercase letters, needs atleast 1.')
            if not hasnumber:
                print('No numbers, needs atleast 1.')
            if not hasspecial:
                print('No special characters, needs atleast 1.')
            return False
                    
bigchoosing = True
while bigchoosing:
    valid = [1,2,3,4]
    choosing = True
    while choosing:
        menukey = int(input('''
1) Create a new User ID
2) Change a password
3) Display all user IDs
4) Quit
'''))
        if menukey in valid:
            choosing = False


        


    choosing2 = True
    if menukey == 1:
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
        
    if menukey == 2:
        choosing4 = True
        f=open('Passwords.csv','r')
        header = f.readline()
        data2 = []
        for line in f:
            data2.append(line.split(', '))
        
        while choosing4:
            olduser = input('Enter your UserID: ')
            if olduser in [user[0] for user in data2]:
                passw = input('Enter a valid password: ')
                if validpassword(passw):
                    choosing4 = False
                    a=open('Passwords.csv','w') #change to write mode to overwrite old password
                    a.write(header)
                    for user in data2:
                        if olduser == user[0]:
                            user[1] = passw+'\n'
                        a.write(user[0]+', '+user[1])
                    a.close()
            else:
                print('UserID not in database, please try again.')
    if menukey == 3:
        f=open('Passwords.csv','r')
        f.readline()
        data2 = []
        print('\nList of all UserIDs in database:\n')
        for line in f:
            print(line.split(', ')[0])
        print()
    if menukey == 4:
        bigchoosing = False
        
        
    
        
#for password change, use list comprehension; if newuser in [user[0] for user in data]:
#repeat function for password check, then append
#for user[0] in data print blah blah