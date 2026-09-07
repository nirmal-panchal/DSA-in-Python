# Count all Digits of a Number

def countDigits(n):
    count = 0
    while n > 0:
        count+=1
        n //= 10

    return count  



print(countDigits(1122))