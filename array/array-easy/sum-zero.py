def sumZero(n):
        temp = []
        for x in range(1, n//2+1):
            temp.append(x)
            temp.append(-x)
        if n % 2 != 0: temp.append(0)
        return temp

print(sumZero(5))