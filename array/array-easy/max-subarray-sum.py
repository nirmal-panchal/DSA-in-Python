# kadane's algorithm

def maxSubArray(nums):
        sum = 0
        maxSum = float('-inf')
        for x in nums:
            sum += x
            maxSum = max(sum, maxSum)
            if sum < 0: sum = 0
        return maxSum
    
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))