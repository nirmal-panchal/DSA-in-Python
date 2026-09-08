# check if currnt is greater than the next
# if yes then swap 
# do this till end, we will get one element sorted at the end of the loop

def bubbleSort(arr):
    n = len(arr)
    
    for i in range(n-1):
        for j in range(n-1):
            if arr[j] > arr[j+1]: 
                arr[j],arr[j+1] = arr[j+1], arr[j]
        

            
arr = [13, 46, 24, 52, 20, 9]
print("before sort:", arr)
bubbleSort(arr)        
print("after sort:", arr)
        

