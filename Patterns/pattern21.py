import math

def pattern21(n):
    for i in range(1):
        for j in range(n):
            print("*", end=" ")

        print()

    for i in range(math.floor(n/2)+1):
        for j in range(n):
            if j == 0 or j == n-1: 
                print("*",end=" ")
            else:
                print(" ",end=" ")

        print()

    for i in range(1):
        for j in range(n):
            print("*", end=" ")


pattern21(4)