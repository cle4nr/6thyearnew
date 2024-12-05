import myMathsLibrary

menulist = [1,2,3,4]
choosing = True
while choosing:
    print('''1. Area of Circle
2. Perimeter of circle
3. Area of rectangle
4. Perimeter of rectangle''')
    menunum = int(input())
    if menunum in menulist:
        choosing = False
if menunum == 1:
    diameter = int(input('Enter your diameter: '))
    circle_area = myMathsLibrary.areacircle(diameter)
    print("Your circle's area:",circle_area)
if menunum == 2:
    diameter = int(input('Enter your diameter: '))
    circle_circum = myMathsLibrary.perimcircle(diameter)
    print("Your circle's perimeter:",circle_circum)
if menunum == 3:
    width = int(input('Enter the width of your rectangle: '))
    height = int(input('Enter the height of your rectangle: '))
    rectarea = myMathsLibrary.rectanglearea(width,height)
    print("Your rectangle's area:",rectarea)
if menunum == 4:
    width = int(input('Enter the width of your rectangle: '))
    height = int(input('Enter the height of your rectangle: '))
    perimrect = myMathsLibrary.rectangleperim(width,height)
    print("Your rectangle's perimeter:",perimrect)
