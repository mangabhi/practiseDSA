def pattern_1():
    for _ in range(1,5):
        for _ in range(1,5):
            print("*",end=" ")
        print()

# pattern_1()

def pattern_2():
    for i in range(1,6):
        for _ in range(i):
            print("*",end=" ")
        print()

# pattern_2()

def pattern_3():
    for i in range(1,6):
        for j in range(1,i+1):
            print(j,end=" ")
        print()

# pattern_3()

def pattern_4():
    for i in range(1,6):
        for _ in range(i):
            print(i,end=" ")
        print()

# pattern_4()

def pattern_5():
    for i in range(5,-1,-1):
        for _ in range(i,-1,-1):
            print("*",end="")
        print()

# pattern_5()

def pattern_6():
    for i in range(5,-1,-1):
        for j in range(1,i+1):
            print(j,end="")
        print()

# pattern_6()

def pattern_7():
    for i in range(0,6):
        #space
        for _ in range(0,6-i-1):
            print(" ",end=" ")
        #star
        for _ in range(0,2*i-1):
            print("*",end=" ")

        for _ in range(0,6-i-1):
            print(" ",end=" ") 

        print()

# pattern_7()

def pattern_8():
    for i in range(0,6):
        #space
        for _ in range(0,i+1):
            print(" ",end=" ")
        #start
        for _ in range(0,2*4-(2*i+1)):
            print("*",end=" ")
        #space
        for _ in range(0,i+1):
            print(" ",end=" ")
        print()

# pattern_8()

def pattern_9():
    pattern_7()
    pattern_8()

# pattern_9()

def pattern_10():
    pattern_2()
    for i in range(0,5):
        for _ in range(5,i+1,-1):
            print("*",end=" ")
        print()

# pattern_10()

def pattern_11():
    ones=1
    for i in range(0,6):
        if i%2==0: ones=1
        else: ones=0
        for _ in range(0,i+1):
            print(ones,end=" ")
            ones = 1- ones
        print()

# pattern_11()

def pattern_12():
    n=4
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end="")
    #space 
        for j in range(2*(n-i)):
            print(" ",end="")

    #left print
        for j in range(i,0,-1):
            print(j,end="")
        print()

# pattern_12()

def pattern_13():
    n=1
    for i in range(1,6):
        for j in range(1,i+1):
            print(n,end=" ")
            n +=1
        print()

# pattern_13()

def pattern_14():
    for i in range(1,6):
        for j in range(i):
            print(chr(65+j),end="")
        print()

# pattern_14()

def pattern_15():
    for i in range(4,0,-1):
        for j in range(0,i+1):
            print(chr(65+j),end="")
        print()

# pattern_15()

def pattern_16():
   for i in range(0,5):
        for j in range(0,i+1):
            print(chr(65+i),end="")
        print()

# pattern_16()



