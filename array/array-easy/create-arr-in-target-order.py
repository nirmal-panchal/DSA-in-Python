def createTargetArray(index, nums):
        target = []
        for i in range(len(nums)):
            target.insert(index[i], nums[i])
        return target

print(createTargetArray([0,1,2,2,1],[0,1,2,3,4]))