# LIST - [], ordered, changeable, duplicate values
# Create a list.
"""
color =["red","orange","Yellow","black","white"]
print(color)"""
"""
color =list((["red","orange","Yellow","black","white"]))
print(type(color))"""

# List item access using index number, it also use negative indexing
"""color =["red","orange","Yellow","black","white"]
print(color[3])
print(color[-1])
print(color[-3])"""

# list item access using range of index
"""color =["red","orange","Yellow","black","white"]
print(color[2:5])
print(color[-4:-1])
print(color[:3])"""

# to check the data or value is present in list using IN
"""color =["red","orange","Yellow","black","white"]
if "orange" in color:
    print("yes, orange is present")"""

# to change the list items
"""color =["red","orange","Yellow","black","white"]
print(color)
#color[1]="pink"
color[2:4]="purple","violet"
print(color)"""

# Insert items in list using insert()
"""fruits =["apple","banana","cherry","grapes","orange"]
print(fruits)
fruits.insert(1,"litchi")
print(fruits)
"""
# add items in list using append() method
"""flower =["rose", "tulip","sunflower","marigold"]
print(flower)
flower.append("delhia")
print(flower)"""

# extend() to add element from one list to another
"""flower=["rose","tulip","lotus","sunflower"]
fruit=["apple","banana","orange","grapes"]
vegetable =("tomato","potato","onion","cabbage","radish")
flower.extend(fruit)
fruit.extend(vegetable)
print(flower)
print(vegetable)
print(fruit)"""

# remove list items using remove()
"""color =["red","orange","Yellow","black","white"]
print(color)
color.remove("red")
print(color)"""

# remove using specified index element using pop()
"""color =["red","orange","Yellow","black","white"]
print(color)
color.pop(1)
print(color)"""

# del() delete specified list
"""color =["red","orange","Yellow","black","white"]
print(color)
#del color[0]
del color
print(color)"""

# clear() empty the list
"""color =["red","orange","Yellow","black","white"]
print(color)
color.clear()
print(color)"""

# Loops in list
"""color =["red","orange","Yellow","black","white"]
for x in color:
    print(x)"""

# for loop using len and range function
"""fruit = ["apple","papaya","guava","watermelon"]
for x in range(len(fruit)):
    print(fruit[x])"""

# while loop
"""color =["red","orange","Yellow","black","white"]
i =0
while i < len(color):
    print(color[i])
    i=i+1"""

# list comphrension offer the shortest syntax for looping through the list
"""lst =[1,4,2,3]
[print(x) for x in lst]"""

# create a new list from an existing list
"""color = ["red","yellow","orange","green","white","black"]
color1 =[]
for x in color:
    if "a" in x:
        color1.append(x)
print(color1)"""

"""color = ["red","yellow","orange","green","white","black"]
color1 =[x for x in color if "e" in x]
print(color1)"""

# Sort() is used to sort the list
"""lst1 =[23,45,23,65,12,8,9,3]
print(lst1)
lst1.sort()
print(lst1)
lst1.sort(reverse=True)
print(lst1)"""










