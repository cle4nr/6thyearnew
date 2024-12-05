def oddseven(r4nge):
    oddlis = []
    evenlis = []
    for i in range(1,r4nge):
        if i%2 != 0:
            oddlis.append(i)
        else:
            evenlis.append(i)
    print(f"Odds = {oddlis}")
    print(f"Evens = {evenlis}")
            
rang3 = int(input('enter a range:	'))
oddseven(rang3)