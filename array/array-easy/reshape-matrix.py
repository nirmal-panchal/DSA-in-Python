def matrixReshape(mat, r, c):
        m = len(mat)
        n = len(mat[0])

        if r*c != m*n : return mat

        temp = []
        for i in range(m):
            for j in range(n):
                temp.append(mat[i][j])

        ans = []
        x = 0
        for i in range(r):
            tmp1 = []
            for j in range(c):
                tmp1.append(temp[x])
                x += 1
            ans.append(tmp1)

        return ans

print(matrixReshape([[1,2],[3,4]], 1, 4))