def nextPermutation(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = -1
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                pivot = i
                break
        
        if pivot == -1:
            nums.reverse()
            return
        
        for i in range(len(nums)-1,-1,-1):
            if nums[i] > nums[pivot]:
                nums[i],nums[pivot] = nums[pivot],nums[i]
                break
        
        nums[pivot + 1:] = nums[pivot + 1:][::-1]
        
        return nums
    
    
print(nextPermutation([1,2,3]))