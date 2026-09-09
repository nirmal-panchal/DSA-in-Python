def setZeroes(matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        freqCol = []
        freqRow = []

        for i in range(len(matrix)):
            if 0 in matrix[i]:
                for j in range(len(matrix[i])):
                    if matrix[i][j] == 0:
                            freqRow.append(i)
                            freqCol.append(j)

        for x in freqRow:
            matrix[x] = [0] * len(matrix[x])
        
        for x in freqCol:
            for y in range(len(matrix)):
                matrix[y][x] = 0
        
        return matrix

print(setZeroes([[1,1,1],[1,0,1],[1,1,1]]))