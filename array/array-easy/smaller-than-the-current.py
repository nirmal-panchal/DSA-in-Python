def smallerNumbersThanCurrent(nums):
        temp = nums.copy()
        temp.sort()
        ans = []
        for x in nums:
            for j in range(len(temp)):
                if temp[j] == x:
                    ans.append(j)
                    break
        
        return ans
    
print(smallerNumbersThanCurrent([8,1,2,2,3]))