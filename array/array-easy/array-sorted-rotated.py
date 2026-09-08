def check(arr):
    spike = 0
    n = len(arr)
    for x in range(n-1):
        if spike > 1: return False
        if arr[x] > arr[x+1]: spike+=1
    
    if arr[0] < arr[n-1]: spike+=1
    
    return spike <= 1
    
arr = [2,1,3,4]
print(check(arr))