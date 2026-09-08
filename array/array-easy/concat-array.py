def getConcatenation(nums):
        n = len(nums)

        for x in range(n):
            nums.append(nums[x])
        
        return nums
    
print(getConcatenation([1,2,1]))