def pattern15(n):
    x = 'A'
    for i in range(n):
        for j in range(n-i):
            print(chr(ord(x) + j), end=" ")
            

        print()

pattern15(5)
            
    