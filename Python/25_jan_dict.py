# Dictionary store data values in key:value pairs.
# dictionary {key:value}, ordered, changeable, dont allow duplicates.

# create a dictionary
"""car ={
    "brand":"ford",
    "model":"mustang",
    "year": 1994,
    "colors":["red","white","blue"]
}
print(type(car), car)
print(len(car))"""

"""thisdict = dict(name="john",age=36, country="Norway")
print(type(thisdict),thisdict)"""

# Access methods in dictionary using key name inside []
"""student ={
    1:"Ram",
    2:"Sham",
    3:"Mohan",
    4:"Krishan"
}
print(student[1])
print(student[2])
print(student[3])
print(student[4])"""

# Access method using get()
"""student ={
    1:"Ram",
    2:"Sham",
    3:"Mohan",
    4:"Krishan"
}
print(student.get(1))
print(student.get(2))
print(student.get(3))
print(student.get(4))"""

# Acces method using keys() - return a list of all the keys in dictionary
"""marks={
    "eng":70,
    "hindi":72,
    "punjabi":74
}
print(marks.keys())
print(marks.values())"""

# access using items()
"""marks={
    "eng":70,
    "hindi":72,
    "punjabi":74
}
print(marks.items())"""

# add value in dictionary
"""car ={
    "brand" : "Maruti",
    "model" : "swift",
    "year" : 2023 
}
print(car.items())
car["color"] = "white"

print(car.items())"""

# check items is available in dictionary or not
"""car ={
    "brand" : "Maruti",
    "model" : "swift",
    "year" : 2023 
}
if "model" in car:
    print("yes, model is present in dictionary")"""

# change values in dictionary
"""bike ={
    "brand" :"bullet",
    "model" :"royal enfield",
    "year" : 2014
}
print(bike)
bike["year"] =2018
print(bike)"""

# update() dictionary
"""marks={
    "eng" : 75,
    "hindi": 75,
    "punjabi": 75
}
print(marks)
marks.update({"punjabi": 70})
print(marks)"""

# Remove items in dictionary using pop()
"""car ={
    "brand" : "Maruti",
    "model" : "swift",
    "year" : 2023 
}
print(car)
car.pop("model")
print(car)"""

# remove items in dictionary using popitem()
"""car ={
    "brand" : "Maruti",
    "model" : "swift",
    "year" : 2023 
}
print(car)
car.popitem()
print(car)"""

# del keyword delete dictionary
"""car ={
    "brand" : "Maruti",
    "model" : "swift",
    "year" : 2023 
}
del car["model"]
print(car)"""

# clear() method empty the dictionary
"""car ={
    "brand" : "Maruti",
    "model" : "swift",
    "year" : 2023 
}
print(car.clear())"""

# loops in dictionary print only the key value
"""car ={
    "brand" : "Maruti",
    "model" : "swift",
    "year" : 2023 
}
for x in car:
    print(x)"""

# this loop gives the values of the dictionary
"""car ={
    "brand" : "Maruti",
    "model" : "swift",
    "year" : 2023 
}
for x in car:
    print(car[x])"""

"""car ={
    "brand" : "Maruti",
    "model" : "swift",
    "year" : 2023 
}
for x in car.keys():
    print(x)
for j in car.values():
        print(j)
for x, y in car.items():
      print(x,y)"""

# copy in dictionary using copy()
"""car ={
    "brand" : "Maruti",
    "model" : "swift",
    "year" : 2023 
}
car1=car.copy()
print(car1)"""

# nested dictionary
"""Top_student ={
    "1st class" :{
        "name" : "jatin",
        "roll.no." : 10
    },
    "2nd class" :{
        "name" :"johny",
        "roll.no" : 8
    },
    "3rd class" : {
        "name" :"karan",
        "roll.no." : 12
    }
}
print(Top_student.keys())
print(Top_student.values())"""

# combine no. of dictionary in to new dictionary
"""car ={
    "brand":"suzuki",
    "model":"dzire",
    "year": 2023
}
bike={
    "brand":"honda",
    "model":"ct 100",
    "year": 2020
}
bus ={
    "brand":"Toyota",
    "model":"Mini bus",
    "year":2024
}
vehicles={
    "car":car,
    "bike":bike,
    "bus":bus
}
print(vehicles.items())
print(vehicles["car"]["model"])
print(vehicles["car"]["brand"])"""
