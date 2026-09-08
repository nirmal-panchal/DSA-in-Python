def findNumbers(nums):
        cnt = 0
        for x in nums:
            if x > 9 and x < 100: cnt+=1
            if x > 999 and x < 10000: cnt+=1
            if x > 99999: cnt+=1
        return cnt

print(findNumbers([12,345,2,6,7896]))