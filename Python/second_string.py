# 1. Capatilize function used to capital the first letter in string
"""x = "hello friends, how are you"
cap=x.capitalize()
print(cap)"""

# 2. Casefold used to small all the capital letters
"""
x = "Hello Friends HOW ARE YOU"
c =x.casefold()
print(c)
"""

# 3. Center() takes word to center according to the given integer value.
"""
x = "Apple"
c=x.center(20)
print(c)
"""

# 4. Count() - this function checks the no. of words(name ) present in list or gives the integer value
"""
x = [1,2,2, 3, 4, 5, 2, 6,2]
c= x.count(2)
print(c)
"""

# 5. encode()  to change the value to encode
"""
c = "Hello Friends How are You"
x=c.encode()
print(c)
print(x)
"""

# 6. endwith() is used to check the list is end with the same value or not gives the output in boolean value
"""c = "Hello Friends How are You."
x=c.endswith("You")
y=c.endswith(".")
print(x)
print(y)"""

# 7. Expandtabs() is used to set the tab space bw the words using \t
"""txt = "\tH\te\tl\tl\to"
c=txt.expandtabs()
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(c)"""

# 8. find() is used to find the string or world or integer value place in the string 
"""lst="Hello Friends How are You"
x=lst.find("Friends")
y=lst.find("are")
print(x)
print(y)"""

# 9. Convert Ankit in to hindi using random library with chr inbuilt function
"""import random
x = random.randint(2300,2378)
a =chr(2309)
n = chr(2367)
k=chr(2325)
i=chr(2306)
t =chr(2340)
print(a,n,k,i,t)
"""

# 10. format() is used to insert the value bw the string
"""txt = "the price of this is {price}"
print(txt.format(price = 49))"""

# 11. To convert the decimal number to binary number used :b format method
"""x = int(input("Enter the Decimal Number : "))
y = "The binary version of {0} is {0:b}"
print(y.format(x))"""

# 12. To convert the decimal number to octal
"""x = int(input("Enter the number: "))
y = "The octal version of {0} is {0:o}"
print(y.format(x))"""

# 13.to convert the decimal number to hexadecimal
"""x = int(input("Enter the number: "))
y = "The Hexadecimal version of {0} is {0:x}"
print(y.format(x))"""


# 14. To convert the decimal number to UTF(UNICODE) used :c format method
"""y = "the binary version of {0} is {0:c}"
print(y.format(2384))
for x in range(10):
    print(y.format(x))"""


# 15. index() is used to search the index value of element
"""x = "Hello Friends"
print(x.index("l"))"""

# 16. isalnum() is used to check the value or string in alpha numeric value
"""x ="abc123de"
y="abc123@#"
print(x.isalnum())
print(y.isalnum())"""

# 17.isalpha() is used to check the value or string is alphabate or not
# isalpha give false value when the space in string
"""x = "MostWelcome"
y = "How are You"
print(x.isalpha())
print(y.isalpha())"""

# 18. isascii(), isdecimal(), isdigit() used to check the value true or not
"""x = "hello world"
y = "123"
print(x.isascii())
print(y.isascii())
print(y.isdigit())
print(x.isdigit())
print(y.isdecimal())"""

# 19. isidentifier() this method is used to check the value is identifier or not
"""x = "the_World4"
y = "123ankit"
print(x.isidentifier())
print(y.isidentifier())"""

# 20.islower() function is used to check the string in lower case
# lstrip() is used to delte the left side spaces
"""txt = "      hello world"
print(txt)
print(txt.islower())
print(txt.lstrip())"""

# 21. isprintable() function is used to check the value is printable or not
"""txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)"""

# 22. isnumeric() method is used to check the numerical value.
# - and . are string value so it give false
"""x= "12345"
y = "1.5"
print(x.isnumeric()) 
print(y.isnumeric())"""

# 23. isspace() is used to check the only blank space in string
"""x ="        "
y= "  s   "
print(x.isspace())
print(y.isspace())"""

# 24. istitle() is used to check the each word having capital letters.
"""txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)"""

# 25. isupper() is used to check the all characters are capital
"""x= "HELLO WORLD"
y= "Hello world"
print(x.isupper())
print(y.isupper())"""

# 26. Join the tuple value in string
"""myTuple = ("John", "Peter", "Vicky")
x = " ".join(myTuple)
print(x)"""
"""lst1 = ["ankit","is","best"]
print(" ".join(lst1))"""

# 27. ljust() and rjust() gives the blank space before the text
"""txt="banana"
x=txt.ljust(10)
print(x,"is fruit")"""

# 28. lower() give upper letter to the lower case letter
"""txt = "HELLO WORLD"
print(txt.lower())"""

# 29. lstrip() is used to left strip
"""x ="    txt"
print(x.lstrip())"""

# 30. maketrans() is used to change the string word
"""txt = "Hello Sam"
txt1= str.maketrans("S","P")
print(txt.translate(txt1))"""

# 31. partition(), rpartition() is used to split string in to three elements 
"""txt = "My name is Ankit Gupta and I live in Rajpura"
x = txt.partition("Ankit Gupta")
print(x)"""

# 32. rfind() method is used to check the right side element
"""txt = "Hello, welcome to my world."
x = txt.rfind("e")
print(x)"""
 