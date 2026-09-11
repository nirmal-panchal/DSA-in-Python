def checkIfExist(arr) -> bool:
        # 1 7 11 14
        arr.sort()
        for x in range(len(arr)):
            s = 0
            e = len(arr) - 1
            while s<=e:
                m = (s+e)//2
                val = arr[x]*2
                if arr[m] == val and m != x: return True
                elif val > arr[m]: s = m + 1
                else: e = m - 1
        return False

print(checkIfExist([10,2,5,3]))