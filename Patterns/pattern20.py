def pattern20(n):
    for i in range(n):

        x = chr(ord('A') + n-i-1) 

        for j in range(i+1):
            print(x, end=" ")
            x = chr(ord(x) + 1)
            
        print()


pattern20(5)