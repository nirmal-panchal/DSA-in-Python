def singleNumber(nums):
        s = set()
        for x in nums:
            if x in s:
                s.remove(x)
            else: s.add(x)
                
        return next(iter(s))
    

print(singleNumber([4,1,2,1,2]))