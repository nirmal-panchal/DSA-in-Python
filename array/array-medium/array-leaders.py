def leaders(arr):
        # code here
        
        currMax = arr[len(arr) - 1]
        temp = []
        temp.append(currMax)
        
        for x in range(len(arr)-2,-1,-1):
            if arr[x] >= currMax:
                temp.append(arr[x])
                currMax = arr[x]
        
        temp.reverse()
        return temp

print(leaders([16, 17, 4, 3, 5, 2]))