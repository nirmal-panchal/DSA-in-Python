def searchInsert(nums, target) -> int:
        s = 0
        e = len(nums) - 1
        ans = 0
        
        if nums[len(nums) - 1] < target: 
            return len(nums)
        
        while s <= e:
            m = (s+e)//2
            if nums[m] >= target:
                ans = m
                e = m - 1
            else:
                s = m + 1
        return ans

print(searchInsert([1,3,5,6], 5))