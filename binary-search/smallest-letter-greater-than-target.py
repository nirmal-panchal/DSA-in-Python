def nextGreatestLetter(target, letters) -> str:
        s = 0
        e = len(letters) - 1
        ans = ''
        if target < letters[0] or target >= letters[e]: return letters[0]
        while s<=e:
            m = (s+e)//2
            if ord(letters[m]) > ord(target):
                ans = letters[m]
                e = m - 1
            else:
                s = m + 1
        return ans


print(nextGreatestLetter("c", ["c","f","j"]))