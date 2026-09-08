# pick the minimum
# swap it with first element
# again pick the minimum from 2nd to end
# swap it with the second element
# do it till end

def selectionSort(arr):
    n = len(arr)
    
    for i in range(n-1):

        el = i
        for j in range(i+1, n):
            if arr[j] < arr[el]: 
                el = j
        
        arr[i],arr[el] = arr[el], arr[i]

            
arr = [13, 46, 24, 52, 20, 9]
print("before sort:", arr)
selectionSort(arr)        
print("after sort:", arr)
        

