def pattern6(n):
    for i in range(n):
        for j in range(n-i):
            print(j+1, end=" ")
        print()

pattern6(5)