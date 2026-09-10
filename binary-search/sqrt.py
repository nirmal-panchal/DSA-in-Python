def mySqrt(x) -> int:
        s = 1
        e = x
        ans = 0
        while s <= e:
            m = (s+e)//2
            val = (m*m)
            if val == x: return m
            elif val < x: 
                ans = m
                s = m + 1
            else: e = m - 1
        return ans

print(mySqrt(4))