def armstrongNum(n):
    x = n
    ans = 0
    
    while x > 0:
        last = x % 10
        x //= 10
        ans += last ** 3
    
    print(ans == n)
    
armstrongNum(153)