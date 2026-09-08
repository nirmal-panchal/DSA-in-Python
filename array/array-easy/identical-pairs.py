from collections import defaultdict

def numIdenticalPairs(nums):
        freq = defaultdict(int)
        ans = 0
        for x in nums:
            ans += freq[x]
            freq[x]+=1
        
        return ans

print(numIdenticalPairs([1,2,3,1,1,3]))