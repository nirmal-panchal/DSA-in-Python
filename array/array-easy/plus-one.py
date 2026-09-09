def plusOne(digits):
        carry = 1
        n = len(digits)

        for x in range(n-1,-1,-1):
            sum = carry + digits[x]
            if sum > 9:
                digits[x] = 0
            else:
                digits[x] = sum
                carry = 0
                break
        
        if carry > 0:
            digits.insert(0,1)

        return digits

print(plusOne([4,3,2,9]))