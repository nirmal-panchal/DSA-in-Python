def maxProfit(prices):
        maxDiff = float('-inf')
        diff = 0
        minPrice = prices[0]
        for x in range(len(prices)):
            if diff < 0: diff = 0
            minPrice = min(minPrice, prices[x])
            diff = prices[x] - minPrice
            maxDiff = max(diff, maxDiff)
        return maxDiff

print(maxProfit([7,1,5,3,6,4]))