def rearrangeArray(nums):
        pos = []
        neg = []

        for x in nums:
            if x > 0: pos.append(x)
            else: neg.append(x)
        
        i = 0
        j = 0
        while i < len(nums)-1:
            nums[i] = pos[j]
            nums[i+1] = neg[j]
            i+=2
            j+=1
        
        return nums

print(rearrangeArray([3,1,-2,-5,2,-4]))