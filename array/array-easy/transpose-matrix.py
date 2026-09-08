def transpose(matrix):
        m = len(matrix)
        n = len(matrix[0])
        ans = []
        for i in range(n):
            temp = []
            for j in range(m):
                temp.append(matrix[j][i])
            ans.append(temp)
        return ans

print(transpose([[1,2,3],[4,5,6],[7,8,9]]))
