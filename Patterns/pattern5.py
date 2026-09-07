def pattern5(n):
    for i in range(n):
        for j in range(n-i):
            print("*", end=" ")
        print()

pattern5(5)