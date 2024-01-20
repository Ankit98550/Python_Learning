# 1. WAP to table
"""table = int(input("Enter the Number"))
for x in range(1,11):
    print(table,"*",x, "=", table*x)"""

# 2. WAP to factor number
"""factor = int(input("Enter the Number"))

for i in range(1,factor+1):
    if factor%i==0:
        print(i)"""

# 3. WAP to factorial number
"""x = int(input("Enter a Number"))
num=1
for a in range(x,1,-1):
    num=num*a 
print(num)    """                     

# 4. WAP to check prime or not prime number
"""num1 =int(input("Enter a number"))
abc =False
if num1 ==1:
    print(num1, "it is not prime number")
elif(num1>0):
    for i in range (2, num1):
        if num1%i==0:
            abc=True
            break
    if abc:
        print(num1, "it is not prime number")
    else:
        print("It is prime number")"""

# 5. WAP to reverse the given string
"""x ="abc123"
v =x[::-1]
print(v)"""


# 6. Count the alphabate and number values
"""txt= input("enter alphanumeric word")
i=0
j=0
k=0
for x in txt:
    if(x.isalpha()):
        i+=1
    elif(x.isdigit()):
        j+=1
    else:
        k+=1
        
print("alphabat and number present in ",txt, "is",i ,"and", j)
print(k,"space")"""

# 7. WAP to check the palindrome
"""txt =input("Enter a Word")
txt1 =txt[::-1] 
if txt1 ==txt:
    print("yes ", txt, "is palindrome")
else:
    print("No ", txt, "is not palindrome")""" 

# 8. WAP to fabonacci series
"""n=9
num1=0
num2=1
next_number=num2
count =1 
while count <= n:
    print(next_number, end=" ")
    count += 1
    num1, num2 = num2, next_number
    next_number = num1 + num2
print()
 """   


"""n =int(input("Enter a number"))
num1 =0
num2 =1
count =1
next_number=num2
while count<=n:
    print(next_number, end=" ")
    count+=1
    num1,num2=num2,next_number
    next_number=num1+num2
print()"""
