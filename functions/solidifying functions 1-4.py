#functions worksheet
import math

def addun(word):
    word1 = 'un' + word
    return word1
#myword = 'plugged'
#print(addun(myword))

def plurals(word):
    word1 = word + 's'
    return word1
#myword2 = 'game'
#print(plurals(myword2))

def areacircle(diam):
    radius = diam / 2
    radsquare = radius * radius
    area = math.pi * radsquare
    return area
#diameter = 2
#print(areacircle(diameter))

def rectanglearea(w,h):
    area = w * h
    return area
#mywidth = 20
#myheight = 10
#print(rectanglearea(mywidth,myheight))

def middlechar(word):
    middlechar = len(word) // 2
    return word[middlechar]
#print(middlechar('joker'))