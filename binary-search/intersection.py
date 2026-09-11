def intersection(nums1, nums2):
        temp = []
        
        for x in nums1:
            if x in nums2 and x not in temp:
                temp.append(x)
        return temp

print(intersection([1,2,2,1], [2,2]))