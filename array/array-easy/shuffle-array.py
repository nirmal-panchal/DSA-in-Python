def shuffle(nums,n):
        m = len(nums)
        temp = []
        for x in range(m//2):
            temp.append(nums[x])
            temp.append(nums[n])
            n+=1
        
        return temp
    
print(shuffle([2,5,1,3,4,7],3));