def secondLargest(arr):
    lg = float('-inf')
    slg = float('-inf')
    i = 0
    n = len(arr)
    
    for i in range(n):
        if arr[i] > lg:
            slg = lg
            lg = arr[i]
        
        elif arr[i] > slg and arr[i] != lg:
            slg = arr[i]
        
    return slg
   
arr = [8, 10, 5, 7, 9]
print(secondLargest(arr))