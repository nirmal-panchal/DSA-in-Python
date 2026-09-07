import math

def isPrime(n):
    count = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0: 
            count+=1
            
            if n // i != i:
                count += 1
    
    print(count == 2)   
    

isPrime(5)     