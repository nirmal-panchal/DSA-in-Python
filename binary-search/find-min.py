def findMin(nums):
        s = 0
        e = len(nums) - 1
        ans = float('inf')
        while s <= e:
            m = (s+e)//2
            if nums[m] > nums[e]:
                s = m + 1
            else:
                e = m - 1
                ans = min(ans,nums[m])
        return ans

print(findMin([3,4,5,1,2]))