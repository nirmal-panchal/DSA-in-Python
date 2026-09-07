
def revNum(x: int) -> int:
        rev = 0
        while x > 0:
            last = x % 10
            x //= 10
            rev = rev*10+last
        
        return rev


def isPalindrome(x: int) -> bool:
        if x < 0: return False

        if revNum(x) != x: return False

        return True 
    

print(isPalindrome(1212))


         