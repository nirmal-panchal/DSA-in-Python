# left Rotate Array by One

def rotateByOne(arr):
    n = len(arr)
    x = arr[n-1]
    
    for i in range(n - 1, -1, -1):
        arr[i] = arr[i-1]
    
    arr[0] = x
    
arr = [9, 8, 7, 6, 4, 2, 1, 3]
print("before rotate :", arr)
rotateByOne(arr)
print("after rotate :", arr)