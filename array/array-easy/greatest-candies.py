def kidsWithCandies(candies, extraCandies):
        maxC = 0
        for x in candies:
            maxC = max(x, maxC)
        
        temp = []
        for x in candies:
            temp.append(x + extraCandies >= maxC)
        
        return temp

print(kidsWithCandies([2,3,5,1,3],3))