def moveZeroes(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        n = len(nums)
        for j in range(n):
            if nums[j] != 0:
                nums[i] = nums[j]
                i+=1
        
        for j in range(i, n):
            nums[j] = 0

arr = [0,1,0,3,12]
print("before rotate :", arr)
moveZeroes(arr)
print("after rotate :", arr)

            