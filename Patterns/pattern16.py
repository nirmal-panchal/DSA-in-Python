def pattern16(n):
    x = 'A'
    for i in range(n):
        for j in range(i+1):
            print(chr(ord(x) + i), end=" ")
            

        print()

pattern16(5)
            
    