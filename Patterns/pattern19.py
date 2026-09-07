def pattern19(n):
    for i in range(n):

        for j in range(n-i):
            print(" ",end=" ")
            
        x = 'A'
        for j in range(2*i+1):
            print(x,end=" ")
            if j < i:
                x = chr(ord(x) + 1)
            else:
                x = chr(ord(x) - 1)

        print()

pattern19(5)