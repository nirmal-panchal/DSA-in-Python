def rotate(mat):
        for i in range(len(mat)):
            for j in range(i+1,len(mat[i])):
                mat[j][i], mat[i][j] = mat[i][j],mat[j][i]
        
        for i in range(len(mat)):
            mat[i].reverse()

def findRotation(mat, target):
        if mat == target: return True
        
        for i in range(3):
            rotate(mat)
            if mat == target: return True
        return False
    
print(findRotation([[0,0,0],[0,1,0],[1,1,1]], [[1,1,1],[0,1,0],[0,0,0]]))