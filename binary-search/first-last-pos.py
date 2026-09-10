def searchRange(nums, target):
        s = 0
        e = len(nums) - 1
        first = -1
        temp = []
        while s <= e:
            m = (s+e)//2
            if nums[m] < target:
                s = m + 1
            else:
                if nums[m] == target:
                    first = m
                e = m - 1
        
        temp.append(first)

        i = 0
        j = len(nums) - 1
        last = -1

        while i <= j:
            m = (i+j)//2
            if nums[m] < target:
                i = m + 1
            else:
                if nums[m] == target:
                    last = m
                    i = m + 1
                else:
                    j = m - 1
        
        temp.append(last)
        return temp

print(searchRange([5,7,7,8,8,10], 8))