def largestElement(arr, i):
    if i == len(arr): return 0
    
    return max(largestElement(arr, i+1), arr[i])
    
arr = [2, 2, 1, 3, 5]
print(largestElement(arr, 0))