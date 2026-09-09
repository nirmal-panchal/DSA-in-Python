def sortColors(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        cntZ = 0
        cntO = 0
        cntT = 0

        for x in nums:
            if x == 0: cntZ+=1
            elif x == 1: cntO += 1
            else: cntT += 1
        i = 0
        while cntZ > 0:
            nums[i] = 0
            cntZ-=1
            i+=1
        while cntO > 0:
            nums[i] = 1
            cntO-=1
            i+=1
        while cntT > 0:
            nums[i] = 2
            cntT-=1
            i+=1
        
        return nums

print(sortColors([2,0,2,1,1,0]))