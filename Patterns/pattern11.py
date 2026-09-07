def pattern11(n):
    for i in range(n):
        x = 0
        if i % 2 == 0: x = 1
        for j in range(i+1):
            print(x, end=" ")
            if x == 0: x = 1
            else: x = 0

        print()

pattern11(5) 

