def searchMatrix(matrix, target) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        lo, hi = 0,m*n-1

        while lo <= hi:
            mid = (lo + hi)//2
            val = matrix[mid // n][mid % n]
            if val == target: return True
            elif val < target: lo = mid + 1
            else: hi = mid - 1
        return False

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))