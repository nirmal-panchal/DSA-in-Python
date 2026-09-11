def peakIndexInMountainArray(arr) -> int:
        # 0 1 2 0
        s = 0
        e = len(arr) - 1
        while s<e:
            m = (s+e)//2
            if arr[m] < arr[m+1]:
                s = m+1
            else: 
                e = m
        return s

print(peakIndexInMountainArray([0,2,1,0]))