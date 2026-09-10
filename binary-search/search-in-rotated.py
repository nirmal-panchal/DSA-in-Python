def search(nums, target):
        s = 0
        e = len(nums) - 1
        while s <= e:
            m = (s+e)//2
            if target == nums[m]: return m
            if nums[s] <= nums[m]:
                if target >= nums[s] and target <= nums[m]:
                    e = m - 1
                else:
                    s = m + 1
            else:
                if target > nums[m] and target <= nums[e]:
                    s = m + 1
                else: 
                    e = m - 1
        return -1

print(search([4,5,6,7,0,1,2], 0))