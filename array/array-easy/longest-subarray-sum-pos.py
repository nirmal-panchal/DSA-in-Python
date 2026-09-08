def longestSubarray(arr, k):
    i = 0
    n = len(arr)
    currSum = 0
    maxArr = arr[i]
    for j in range(n):
        currSum += arr[j]
        
        while currSum > k:
            currSum -= arr[i]
            i += 1
        
        if currSum == k:
            maxArr = max(maxArr, j - i + 1)
            
    return maxArr
    
print(longestSubarray([2, 3, 5, 1, 1, 1, 1], 7))