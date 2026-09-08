def union(arr1, arr2):
    m = len(arr1)
    n = len(arr2)

    temp = []
    i = 0
    j = 0

    while i < m and j < n:

        if arr1[i] < arr2[j]:
            if not temp or temp[-1] != arr1[i]:
                temp.append(arr1[i])
            i += 1

        elif arr2[j] < arr1[i]:
            if not temp or temp[-1] != arr2[j]:
                temp.append(arr2[j])
            j += 1

        else:
            # Both are equal
            if not temp or temp[-1] != arr1[i]:
                temp.append(arr1[i])

            i += 1
            j += 1

    while i < m:
        if not temp or temp[-1] != arr1[i]:
            temp.append(arr1[i])
        i += 1

    while j < n:
        if not temp or temp[-1] != arr2[j]:
            temp.append(arr2[j])
        j += 1

    return temp


arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 3, 4, 4, 5]

print("union:", union(arr1, arr2))