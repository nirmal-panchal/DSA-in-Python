def minEatingSpeed(piles, h) -> int:
        s = 1
        e = 0
        for x in piles:
            e = max(x, e)
        ans = 0

        while s <= e:
            m = (s+e)//2
            cnt = 0
            for x in piles:
                cnt += (x + m - 1) // m
            
            if cnt <= h:
                e = m - 1
                ans = m
            else:
                s = m + 1
        return ans

print(minEatingSpeed([3,6,7,11], 8))