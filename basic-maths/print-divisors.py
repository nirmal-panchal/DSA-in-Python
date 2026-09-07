import math

def printDivisors(n):
    res = []
    
    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            res.append(i)
            
            if i != n:
                res.append(n // i)
    
    print(res)
    
    
printDivisors(36)