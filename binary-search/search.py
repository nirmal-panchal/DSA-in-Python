def search(nums, target) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == target: return m
            elif nums[m] < target: i = m + 1
            else: j = m - 1
        return -1

print(search([-1,0,3,5,9,12], 9))