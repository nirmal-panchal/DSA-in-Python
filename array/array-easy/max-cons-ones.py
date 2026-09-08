def findMaxConsecutiveOnes(nums):
        currOnes = 0 
        maxOnes = 0

        for x in nums:
            if x == 1:
                currOnes+=1
            else:
                maxOnes = max(maxOnes, currOnes)
                currOnes = 0
        
        return max(maxOnes, currOnes)
    
print(findMaxConsecutiveOnes([1,1,0,1,1,1]))