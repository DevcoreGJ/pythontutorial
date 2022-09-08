import os
os.system('clear')
'''
#########################################
#INTRO
#########################################

#vars

first_name = "John"
#########################################
#outputs
print(first_name) #output
#########################################
#########################################
#OVERLOADING VARS
#########################################
#ORIGINAL
first_name = "John" 
print(first_name)
#OVERLOADED
first_name = "Bob" 
print(first_name)
'''
'''
#########################################
#HELLO WORLD
#########################################
#prints out hello world to the screen
prints variable
print("Hello World!")
#########################################
'''
#########################################
# DATA TYPES
# Strings
# Numbers
# Lists
# Tuples
# Dictionaries
# Boolean
#########################################
'''
#########################################
#STRING
#########################################
first_name = 'john' #VAR STRING
'''
'''
#########################################
NUMBERS
#########################################
age = 41 #VAR INT
'''
'''
#########################################
#LISTS
#########################################
names = ["John","Bob","Mary"] #LIST DATA TYPE HOLDING STRINGS
print(names[0]) #PRINTS JOHN
'''
'''
#########################################
#TUPLES
#########################################
names = ("John","Bob","Mary") #TUPLE DATA TYPE HOLDING STRINGS
print(names) #PRINTS ALL NAMES IN TUPLE
'''
'''
#########################################
#DICTIONARIES
#########################################
fav_pizza = {	#DICTIONARY DATA TYPE CONTAINING KEY VAL PAIRS
	"John": "Pepperoni",
	"Bob": "Mushroom",
	"Mary": "Cheese"
	}

print (fav_pizza["John"]) PRINTS VALUE OF JOHN IN DISCTIONARY
'''
'''
#########################################
#BOOLEAN
#########################################

name = True 

print (name)
'''
'''
#########################################
#FUNCTINAL MODIFIERS
#########################################
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
'''
#########################################
#NUMBERS
#########################################
#integers
num = 10
print(int(num))
'''
'''
#########################################
#floats
#########################################
num=10.25
print(float(num))
'''
'''
#########################################
#MATH
#########################################
num_1 = 5
num_2 = 2
num_3 = "113"
print((int(num_3)*num_1*num_2)) # prints result whilst also converting num_3 to int

print(num_3*3) # duplicating string by multiplier
'''
'''
#########################################
#LISTS
#########################################

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
'''
##########################################
#tuples
##########################################

tuple1 = ("John", "Bob", "Tina")
tuple2 = ("Mary",)
tuple3 = tuple1 + tuple2
tuple4 = tuple1[0:2] + tuple2

print(tuple1[0])
print(tuple3)
print(tuple1[0:2])
print(tuple4)
'''
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
'''
'''
##########################################
#assignment operators
#########################################
# = assigning something to the variable/function
# +=
# -=
# *=
# /=
# **=
# %=
#########################################
'''
'''
num = 41

num += 1 # num = num + 1

print(num + 1)
print(num)
'''
'''
#########################################
#Comparison Operators
#########################################
# ==
# !=
# >
# <
# >=
# <=
#########################################
'''
'''
print(10 == 10)

print(10 != 9)

print(10<=9)

print([1,2,3,4] == {1,2,3,4,5})
'''
'''
#########################################
#########################################

#########################################
#Conditional Statements

# if
# else
# elif
#########################################
# input vars
num = 5 # input
#########################################
#output vars
condition1Met = "your number is greater than 10!" #output1
condition1NotMet = "your number is less than 10!" #output2
condition1Perfect = "your number is 10!" #output3
#########################################
#loops
if(num > 10): #initial if
	print(condition1Met.title())
elif(num == 10): #initial elif
	print(condition1Perfect.title())
else:
	print(condition1NotMet.title()) #initial else
'''
'''
#########################################
#########################################
#multiple conditional statements
#########################################
#and
#or
#########################################
# input vars
num = 7 # input
#########################################
#output vars
conditions = [
condition1Met := "your number is greater than 10!", #conditon1output0
condition1NotMet := "your number is less than 10!", #conditon1output1
condition1Perfect := "your number is 10!", #conditon1output2
#and conditions
condition2Met := "your number is greater than 100!", #conditon2:output3
condition2NotMet := "your number is not greater than 100!", #condition2:output4
condition2Perfect := "your number is 100", #condition2:output5
#or conditions
condition3Met := "Your number is greater than 10 but not greater than 100", #condition3:output6
condition3NotMet := "your number is greater than 1 but not greater than 10", #condition3:output7
condition3PartMet := "your number is not greater than 1", #condition3:output8
]
#########################################
#loops
#########################################
#for loop
#########################################
for i in range (len(conditions)): #conditions = list name
	conditions[i] = conditions[i].title() #list items title case
#########################################
#if loop
#########################################
if (num > 10):
	print(conditions[0])

elif (num < 10):
	print(conditions[1])

elif (num == 10):
	print (conditions[2])

elif (num > 10) and (num > 100):
	print(conditions[0] and [3])

elif (num > 10) and (num < 100):
	print(conditions[0] and [4])
				
elif(num == 100):
	print(conditions[5])

########################################

if (num > 1 < 10) or (num < 1):
	print(conditions[7] or [8])

elif (num > 10) or (num > 100):
	print(conditions[6] or [3]) #>10 or >100

elif (num < 10) or (num < 100):
	print(conditions[0] or [4])
'''
'''
#########################################
#########################################
#WHILE
#########################################
#input vars

#########################################
#output vars
countList = [
strOut:= "the count is: ",
counter := 0,
]	
#########################################
#methods
while (countList[1] < 10):
	print(countList[0].title() + str(countList[1]))
	countList[1] += 1

#########################################
'''

########################################
#########################################
#FOR
#########################################
#input vars
#names = "John", "Bob", "Mary"
fav_pizza = {
	"John": "pepperoni",
	"Bob": "margarita",
	"Mary": "sausage",
}
#########################################
#methods:

#name and topping ranging the length in dictionary fav_pizza
#dictionary items capitalcase key and value
for key,value in fav_pizza.items(): 
	fav_pizza[key,value.capitalize()] = fav_pizza.pop(key,value).capitalize()

#for name in names:
#	print(name[0])
	print(key + " likes " + value + " pizza.")
#########################################

