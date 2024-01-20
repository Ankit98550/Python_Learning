# 1. Program to print half pyramid using *
"""num = int(input("Enter a number"))
for x in range(1,num+1):
    for j in range(1, x+1):
        print("*", end="")
    print("\n)"""

#2. WAP to print half pyramid using number
"""num =3
for x in range(1,num+1):
    for j in range(1, x+1):
        print(j,end="")
    print("\n")"""

#3. WAP to print half pyramid using alphabets
"""num=65
num1 =int(input("Enter a number"))
for x in range(num,num+num1):
    for j in range(num,x+1):
        k=chr(j)
        print(k,end=" ")    
    print()"""

#4. WAP to print half pyramid using alphabets as A, BB,CCC
"""row = int(input("Enter value"))
ascii_value =65
for x in range(1,row+1):
    for j in range(1,x+1):
        alpha=chr(ascii_value)
        print(alpha, end="")
    ascii_value+=1
    print()     """   

#5.WAP to pyramid using character a,bc, def
"""row = int(input("Enter a number"))
ascii_value=65
for x in range(1, row+1):
    for j in range(1, x+1):
        alpha =chr(ascii_value)
        print(alpha, end="")
        ascii_value+=1
    print()"""

#6. WAP to inverted pyramid using *
"""row = int(input("Enter a number"))
for x in range(row, 0, -1):
    for j in range(1,x+1):
        print("*", end="")
    print()"""

#7. WAP to inverted pyramid using numbers as 4321,321,21,1
"""row = int(input("Enter number"))
for i in range(row, 0,-1):
    for j in range(i,0,-1):
        print(j,end="")
    print()"""

#8. WAP to full Pyramid using *
"""k=0
row = int(input("Enter number"))
for i in range(1,row+1):
    for space in range(1,(row-i)+1):
        print(end="  ")
    while k!=(2*i-1):
        print("* ",end="")
        k += 1
    k=0
    print()"""


# Make Simple  Triange pyramid 1, 1 2, 1 2 3
"""x = int(input("Enter the number"))
num =1
for i in range(1,x+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print("\n")"""

# Make Pyramid by addition 1, 2 3, 4 5 6
"""x = int(input("Enter the number"))
num =1
for i in range(1,x+1):
    for j in range(1,i+1):
        print(num, end=" ")
        num+=1
    print("\n")"""

# Pyramid 1, 2 2, 3 3 3
"""x = int(input("Enter a number"))
num =1
for i in range(1,x+1):
    for j in range(1,i+1):
        print(num,end=" ")
    num +=1
    print("\n")"""

# Pyramid using Characters
"""num =int(input("enter a number"))
x =65
v =chr(x)
for i in range(1,num+1):
    for j in range(1,i+1):
        print(v, end=" ")
    print(v)"""

# Pyramid using characters A, B C, D E F
"""row = int(input("enter number"))
num=65
for x in range(1, row+1):
    for j in range(1, x+1):
        alpha =chr(num)
        num+=1
        print(alpha, end=" ")
    print()"""

# Pyramid characters a, b b ,c c c
"""row = int(input("enter number"))
num=65
for x in range(1, row+1):
    for j in range(1, x+1):
        alpha =chr(num)
        print(alpha, end=" ")
    num+=1
    print()"""

# pyramid characters a, ab, abc, abcd
"""num = int(65)
num2=chr(num)
num1=int(input("enter a number"))
for x in range(num, num+num1):
    for j in range(num,x+1):
        k=chr(j)
        print(k, end=" ")
        
    print()"""

# Reverse the pyramid 1234, 123,12,1
"""num =int(input("enter a number"))
for x in range(num,0,-1):
    for j in range(1,x+1):
        print(j, end="")
    print()"""

num =int(input("enter a number"))
for x in range(1, num+1):
    for j in range(1,x+1):
        print(" ", end="")
    for k in range(1, j+1):
        print(k, end=" ")
        
    print()
