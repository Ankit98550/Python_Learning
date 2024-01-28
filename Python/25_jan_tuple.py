# tuple are ordered, unchangeable, allow duplicate ,()
# Create a tuple
"""color =("red","orange","black","white","purple")
tuple1 =("red","orange",23, 45, True)
fruit = tuple(("apple","banana","mango","orange"))
print(type(color))
print(len(color))"""

# Access method in tuple
"""print(tuple1[3])
print(type(fruit))"""

# Negative Indexing 
"""print(tuple1[-2])
print(tuple1[2:4])
print(fruit[:3])"""

# Check item exist in tuple
"""flower=("rose","tulip","marigold","sunflower")
if "rose" in flower:
    print("yes, is persent in list")"""

# Change tuple value "to change the tuple values first convert to list"
"""name = ("Ram","Sham","Mohan","Krishan")
name1 = list(name)
print(name)
print(type(name1))
name1[3] ="Rajesh"
name1.append("Ganesh")
name1.insert(4,"Shiv")
name = tuple(name1)
print(type(name))"""

# add tuple in to tuple
"""fruit=("apple","banana","mango","litchi")
fruit1 =("guava","grapes","peach","watermelon")
fruit +=fruit1
print(fruit)"""

# Remove item from tuple
"""fruit=("apple","banana","mango","litchi")
fruit1 = list(fruit)
fruit1.remove("apple")
fruit1.pop(2)
fruit=tuple(fruit1)
print(fruit1)"""

# Unpacking a tuple
"""num =(9855,97810,62789)
(ram, ankit,rohit) =num
print(ram)"""

# For loop in tuple
"""fruit=("apple","banana","mango","litchi")
for x in fruit:
    print(x)
print()
for j in range(len(fruit)):
    print(fruit[j])"""

# While loop
"""fruit=("apple","banana","mango","litchi")
i=0
while i<len(fruit):
    print(fruit[i])
    i+=1"""

# join two tuple using + operator
"""a =("a","b","c","d")
b =(1,2,3,4)
c =a+b
print(c)
d =a*2
print(d)"""

