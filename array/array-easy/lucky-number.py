
# A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

def luckyNumbers(matrix):
        tempMin = []
        tempMax = []

        c = len(matrix)
        r = len(matrix[0])

        for i in range(c):
            minVal = matrix[i][0]
            for j in range(r):
                minVal = min(minVal, matrix[i][j])
            tempMin.append(minVal)
        
        for i in range(r):
            maxVal = 0
            for j in range(c):
                maxVal = max(maxVal, matrix[j][i])
            tempMax.append(maxVal)
        
        s = set(tempMin)
        for x in range(len(tempMax)):
            if tempMax[x] in s:
                return [tempMax[x]]

        return []

print(luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))