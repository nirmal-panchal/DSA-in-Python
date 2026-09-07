def revNum(x: int) -> int:
        rev = 0
        while x > 0:
            last = x % 10
            x //= 10
            rev = rev*10+last
        
        return rev

print(revNum(1234))