def rowWithMax1s(arr) -> int:
        # code here
        
        maxOnes = 0
        ansIdx = 0
        m = len(arr)
        n = len(arr[0])
        for x in range(m):
            if arr[x][0] == 1: return x
            else:
                s = 0
                e = n - 1
                while s<=e:
                    m = (s+e)//2
                    if arr[x][m] == 1:
                        idx = m
                        e = m - 1
                    else:
                        s = m + 1
                if(n - s > maxOnes):
                    maxOnes = n - idx
                    ansIdx = x
                
                    
        if ansIdx == 0:
            if 1 in arr[0]:
                return ansIdx
            else: return -1
        
        return ansIdx

print(rowWithMax1s([[0,1,1,1], [0,0,1,1], [1,1,1,1]]))