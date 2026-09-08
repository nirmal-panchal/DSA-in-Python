def insertionSort(arr):
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]
        j = i-1
        
        while j>=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = key


            
arr = [13, 46, 24, 52, 20, 9]
print("before sort:", arr)
insertionSort(arr)        
print("after sort:", arr)
        

