#recursive functions
def listsum(l):
    n = l.pop(0) #removes 1st item in list and stores as n
    if len(l) > 1: #if length of list is more than 1
        return n + listsum(l) #returns 1st item of list 
    else: #if all numbers of list have been gone through
        return n + l[0]

def intsum(i):
    if i>1:
        return i + intsum(i-1)
    else:
        return 1

def has_num(s):
    if s[0].isdigit():
        return True
    elif len(s) == 1:
        return False
    else:
        return has_num(s[1:])
    
print(listsum([1,7,6,3,4]))
print(intsum(6))
print(has_num("lmnoopqrs9"))
