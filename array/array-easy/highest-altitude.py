def largestAltitude(gain):
        sum = 0
        maxSum = 0
        for x in gain:
            sum += x
            maxSum = max(sum, maxSum)
        
        return maxSum

print(largestAltitude([-5,1,5,0,-7]))