
# we have to subtract the smaller number withe greater number until any one becomes 0

def printGCD(x,y):
    smaller = min(x,y)
    greater = max(x,y)
    
    while smaller > 0 and greater > 0:
        greater = min(greater - smaller, smaller)
        smaller = greater - smaller
    
    print(greater)


printGCD(20,15)
        