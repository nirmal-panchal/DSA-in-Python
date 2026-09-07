def reverseArray(arr, i, j):
    if i>=j: return
    
    arr[i],arr[j] = arr[j],arr[i]
    
    reverseArray(arr,i+1,j-1)
    
    
arr = [1,2,3,4]
reverseArray(arr, 0 ,len(arr)-1)
print(arr)