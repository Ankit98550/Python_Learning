# Sets are used to store multiple items in single variable
# Sets -{}, unchangeable, unordered, unindexed, duplicate not allowed
"""fruits ={"apple","banana","litchi","apple"}
print(type(fruits),fruits)
print(len(fruits))

color = set(("red","orange","green","pink"))
print(type(color),color)
"""

# Set having different data types
"""thisset = {"Ankit","Rohit",98500,76260,True}
print(thisset)"""

# set items are not access by there index number
"""flower = {"rose","tulip","delhia","marigold","lotus"}
for x in flower:
    print(x)"""

# Check value is present or not in set
"""thisset = {"apple","banana","cherry"}
print("banana" in thisset)"""

# add() item in set
"""sports ={"cricket","hockey","carrom board","football"}
print(sports)
sports.add("baseball")
print(sports)
"""
# add two set using update() method
"""flower = {"daisy","lavender","lotus","daffodil","peony"}
flower1 ={"rose","lily","bluebell"}
print(flower)
flower.update(flower1)
print(flower)"""

# delete items in set using remove()
"""fruit ={"apple","banana","papaya","orange","pineapple"}
print(fruit)
fruit.remove("apple")
print(fruit)"""

# remove using discard() method
"""fruit ={"grapes","watermelon","litchi","guava","date","mango","cherry"}
print(fruit)
fruit.discard("grapes")
print(fruit)"""

# remove using pop() method delete random item
"""flowers ={"hibiscus","marigold","sunflower","dahlia","jasmine"}
print(flowers)
flowers.pop()
print(flowers)"""

# clear, del() method clear or delete the set
"""flowers ={"hibiscus","marigold","sunflower","dahlia","jasmine"}
flowers.clear()
del flowers
print(flowers)"""

# join sets using union() and update()
"""set1 = {"a","b","c","d"}
set2 = {1,2,3,4}
set3 = set1.union(set2)
print(set3)"""

"""num ={1,2,4,5,6}
alpha ={"a","b","c","d"}
print(num)
print(alpha)
num.update(alpha)
print(num)"""

# intersection() method is used to check the same value in two set
"""company ={"google","microsoft","apple"}
fruit ={"banana","apple","orange"}
company.intersection_update(fruit)
print(company)"""

"""company ={"google","microsoft","apple"}
fruit ={"banana","apple","orange"}
z=company.intersection(fruit)
print(z)"""

# symmetric_difference_update() method give the different value from two elements
"""company ={"google","microsoft","apple"}
fruit ={"banana","apple","orange"}
company.symmetric_difference_update(fruit)
print(company)"""

