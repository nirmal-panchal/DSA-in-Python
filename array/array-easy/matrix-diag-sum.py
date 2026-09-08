def diagonalSum(mat):
        m = len(mat)
        sum = 0
        for x in range(m):
            sum += mat[x][x]
            sum += mat[m-1][x]
            m-=1
        if len(mat) % 2 != 0: 
            return sum - mat[len(mat)//2][len(mat)//2]
        return sum

print(diagonalSum([[1,2,3],
              [4,5,6],
              [7,8,9]]))