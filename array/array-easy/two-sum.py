def twoSum(nums,target):
        mpp = dict()
        for i in range(len(nums)):
            key = target - nums[i]
            if key in mpp:
                return [mpp[key], i]
            mpp[nums[i]] = i
        return [-1,-1] 

print(twoSum([2,7,11,15],9))