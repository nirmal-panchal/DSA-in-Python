def missingNumber(nums):
        n = len(nums)

        totalSum = (n * (n+1))//2
        currSum = 0
        for x in nums:
            currSum+=x
        
        return totalSum - currSum

print(missingNumber([3,0,1]))