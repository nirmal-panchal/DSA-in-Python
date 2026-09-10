def singleNonDuplicate(nums):
        s = 0
        e = len(nums)-1
        while s <= e:
            m = (s+e)//2
            if m % 2 == 0:
                if nums[m] == nums[m-1]:
                    e = m - 1
                else:
                    s = m + 1
            else:
                if nums[m] == nums[m-1]:
                    s = m + 1
                else:
                    e = m - 1

        return nums[e]

print(singleNonDuplicate([1,1,2,3,3,4,4,8,8]))