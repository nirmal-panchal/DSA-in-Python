def isPalindrome(str, i, j):
    if i>=j: return True
    if str[i] != str[j]: return False
    return isPalindrome(str, i+1, j-1)
    
str = "nayan"
print(isPalindrome("nayan", 0, len(str) - 1))