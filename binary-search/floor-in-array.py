def findFloor(arr, x):
        # code here
                s = 0
                e = len(arr) - 1
                ans = 0

                if arr[0] > x: 
                    return -1

                while s <= e:
                    m = (s+e)//2
                    if arr[m] <= x:
                        ans = m
                        s = m + 1
                    else:
                        e = m - 1
                return ans

print(findFloor([1, 2, 8, 10, 10, 12, 19],5))