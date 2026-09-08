def buildArray(nums):
        temp = []
        for i in range(len(nums)):
           temp.append(nums[nums[i]])
        return temp

print(buildArray([0,2,1,5,3,4]))