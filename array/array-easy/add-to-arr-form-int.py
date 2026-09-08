def addToArrayForm(num, k):
        for x in range(len(num)-1, -1, -1):
            k += num[x]
            last = k % 10
            num[x] = last
            k //= 10
        
        while k > 0:
            last = k % 10
            num.insert(0, last)
            k //= 10
        return num

print(addToArrayForm([1,2,0,0], 34))