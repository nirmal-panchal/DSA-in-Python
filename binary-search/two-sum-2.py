def twoSum(numbers, target):
        for i in range(len(numbers)):
            val = target - numbers[i]
            s = i + 1
            e = len(numbers)-1

            while s <= e:
                m = (s+e)//2
                if numbers[m] == val:
                    return [i+1, m+1]
                elif val > numbers[m]:
                    s = m + 1
                else: e = m - 1
        return []

print(twoSum([2,7,11,15], 9))