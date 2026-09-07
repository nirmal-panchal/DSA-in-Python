def pattern12(n):
    for i in range(n):
        for j in range(i+1):
            print(j+1, end=" ")

        for j in range(2 * (n-i-1)):
            print(" ", end=" ")

        for j in range(i + 1):
            print(i - j + 1, end=" ")

        print()
        


pattern12(5)