from collections import defaultdict

def majorityElement(nums):
        d = defaultdict(int)
        n = len(nums)
        for x in nums:
            d[x] += 1
        
        for x in d:
            if d[x] > n//2:
                return x
        
        return -1

print(majorityElement([3,2,3]))