import os
os.system('clear')
####################
#variables declared
'''
first_name = "John"
#print(first_name)
'''
###################
###################
'''
first_name = "John"
#print(first_name)
#first_name = "Bob"
#print(first_name)
'''
###################
#####################################
#prints out hello world to the screen
#prints variable
#print("Hello World!")
#####################################

####################################
# DATA TYPES
# Strings
# Numbers
# Lists
# Tuples
# Dictionaries
# Boolean
####################################
#string
#first_name = 'john'
#numbers
#age = 41
'''
#lists
names = ["John","Bob","Mary"]
print(names[0])
#tuples
names = ("John","Bob","Mary")
print(names)
'''
#Dictionaries
'''
fav_pizza = {
	"John": "Pepperoni"
	,
	"Bob": "Mushroom",
	"Mary": "Cheese"
	}
print (fav_pizza["John"])
#Boolean

name = True

print (name)
'''
'''
greetings = 'Hello, my name is John Elder'

print (greetings.upper())
print (greetings.lower())
print (greetings.capitalize())
print (greetings.title())
print (greetings.swapcase())
print(len(greetings))
'''
'''
print(greetings[13])
print(greetings[18:22])

print(greetings.split(" ")[5])
print(greetings.split(" ")[4:6])
'''
########################################
#numbers
########################################
#integers
'''
num = 10
print(int(num))
#floats
num=10.25
print(float(num))
#10.25
#doubles
#math
num_1 = 5
num_2 = 2
num_3 = "113"
print((int(num_3)*num_1*num_2)) # prints result whilst also converting num_3 to int

print(num_3*3) # duplicating string by multiplier
'''
########################################
#Lists
########################################
'''
otherName = "Nic"
names = ["John", "Bob", "Tina", 41, otherName]
names[0] = "Wes"
print(names[0])
print(names)
names.append("John")
print(names)
print(names[3])
names.append(int(27))
example = 23.9
names.append(example)
nums = [1,2,3,4,5]
names.append(nums)

print(names)

print(len(nums))
'''
##########################################
#tuples
##########################################
'''
tuple1 = ("John", "Bob", "Tina")
tuple2 = ("Mary",)
tuple3 = tuple1 + tuple2
tuple4 = tuple1[0:2] + tuple2

print(tuple1[0])
print(tuple3)
print(tuple1[0:2])
print(tuple4)
'''
############################################
#dicttionaries
############################################
favourite_pizza = {
	"ben":	"pepperoni",
	"lisa":	"margarita",
	"tim":	"sausage",
}
del favourite_pizza["ben"]
favourite_pizza.update({"Tina":"Green Peppers"})
print(favourite_pizza)
print(favourite_pizza["Tina"])
favourite_pizza["John"] = "Green Peppers"
print(favourite_pizza)
