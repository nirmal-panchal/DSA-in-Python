def countNegatives(grid) -> int:
        c = 0
        for x in range(len(grid)):
            if grid[x][0] < 0:
                c += len(grid[x])
            else:
                s = 0
                temp = 0
                e = len(grid[x]) - 1
                while s<=e:
                    m = (s+e)//2
                    if grid[x][m] >= 0:
                        s = m + 1
                    else: 
                        temp = m
                        e = m - 1
                if temp > 0 : c += (len(grid[x]) - temp)
        return c


print(countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))