def findPeakElement(nums):
        s = 0
        e = len(nums) - 1
        while s<e:
            m = (s+e)//2
            if nums[m] < nums[m+1]:
                s = m + 1
            else: e = m
        return s

print(findPeakElement([1,2,3,1]))