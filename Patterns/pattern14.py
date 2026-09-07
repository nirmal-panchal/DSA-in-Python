def pattern14(n):
    x = 'A'
    for i in range(n):
        for j in range(i+1):
            print(chr(ord(x) + j), end=" ")
            

        print()

pattern14(5)
            
    