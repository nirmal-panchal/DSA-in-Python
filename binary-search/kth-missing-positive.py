def findKthPositive(arr, k) -> int:
        s = 0
        e = len(arr) - 1
        while s <= e:
            m = (s+e)//2
            missing = arr[m] - (m+1)
            if missing < k:
                s = m + 1
            else:
                e = m - 1
        return e + k + 1

print(findKthPositive([2,3,4,7,11], 5))