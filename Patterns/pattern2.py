def pattern2(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end=" ")
        print()


pattern2(5)