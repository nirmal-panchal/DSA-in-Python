def pattern13(n):
    x = 1
    for i in range(n):
        for j in range(i+1):
            print(x, end=" ")
            x+=1

        print()

pattern13(5)
            
    