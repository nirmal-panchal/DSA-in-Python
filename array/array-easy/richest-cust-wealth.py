def maximumWealth(accounts):
        maxSum = 0
        m = len(accounts)
        for i in range(m):
            
            n = len(accounts[i])
            currSum = 0
            
            for j in range(n):
                currSum += accounts[i][j]
            
            maxSum = max(currSum, maxSum)
        
        return maxSum
    
print(maximumWealth([[1,5],[7,3],[3,5]]))