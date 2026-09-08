def rotate(arr, k):
    arr[:] = arr[::-1]
    arr[:k] = arr[:k][::-1]
    arr[k:] = arr[k:][::-1]
    

arr = [1,2,3,4,5,6,7]
print("before rotate :", arr)
rotate(arr, 3)
print("after rotate :", arr)