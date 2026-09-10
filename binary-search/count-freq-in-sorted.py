def countFreq(arr, target):
        # code here
                s = 0
                e = len(arr) - 1
                first = -1
                while s <= e:
                    m = (s+e)//2
                    if arr[m] < target:
                        s = m + 1
                    else:
                        if arr[m] == target:
                            first = m
                        e = m - 1


                i = 0
                j = len(arr) - 1
                last = -1

                while i <= j:
                    m = (i+j)//2
                    if arr[m] < target:
                        i = m + 1
                    else:
                        if arr[m] == target:
                            last = m
                            i = m + 1
                        else:
                            j = m - 1

                if last == -1 or first == -1 : return 0
                return last - first + 1
    
print(countFreq([1, 1, 2, 2, 2, 2, 3],2))