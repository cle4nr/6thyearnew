f = open('ufc-fighters-statistics-cut.csv')
header = f.readline()
dic = {}
masterdict = {}



# headlist = header.split(',')
# for x in range(len(headlist)):
#      print(headlist[x],x)

strip = []
for line in f:
    line = line.split(',')
    print(line)

    


def weightcheck(weight):
    if weight > 94:
        return "heavyweight"
    elif weight > 84:
        return "lightheavyweight"
    elif weight > 78:
        return "middleweight"
    elif weight > 71:
        return "welterweight"
    elif weight > 66:
        return "lightweight"
    elif weight > 62:
        return "featherweight"
    elif weight > 58:
        return "bantamweight"
    else:
        return "flyweight"
    

    
    

    
    
