def rotate(matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        for x in range(m):
            for y in range(x+1, n):
                matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]
            matrix[x].reverse()
        
        return matrix


print(rotate([[1,2,3],[4,5,6],[7,8,9]]))