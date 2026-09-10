def upperBound(arr, target):
         # code here
                s = 0
                e = len(arr) - 1
                ans = 0

                if arr[len(arr) - 1] < target:
                    return len(arr)

                while s <= e:
                    m = (s + e) // 2
                    if arr[m] > target:
                        ans = m
                        e = m - 1
                    else:
                        s = m + 1
                return ans

print(upperBound([2, 3, 7, 10, 11, 11, 25], 9))