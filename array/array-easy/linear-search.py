def linearSearch(arr, k):
    n = len(arr)
    for x in range(n):
        if arr[x] == k: return x;
    
    return -1

arr = [1,2,3,4,5]
print(linearSearch(arr, 7))