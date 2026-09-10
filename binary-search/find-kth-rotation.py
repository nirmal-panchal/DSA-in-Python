def findKRotation(arr):
        # code here
            s = 0
            e = len(arr) - 1
            ans = float('inf')
            minIdx = 0
            
            if arr[s] <= arr[e]: return 0
            
            while s <= e:
                m = (s+e)//2
                if arr[m] > arr[e]:
                    s = m + 1
                else:
                    if arr[m] < ans:
                        ans = arr[m]
                        minIdx = m
                    e = m - 1
            return minIdx
    
print(findKRotation([5, 1, 2, 3, 4]))