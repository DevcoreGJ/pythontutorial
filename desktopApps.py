import os
os.system('clear')
#import namer
from namer import namer #from file name import function
import sqlite3
from tkinter import *
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
'''
#########################################
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
'''

#########################################
#########################################
#FIZZBUZZ
#WHAT IS FIZZBUZZ?
'''
FIZZBUZZ IS A TECH TEST
THE AIM IS TO PRINT NUMS 0-100 OUT ON TO THE SCREEN
IF DIVISABLE BY 3 PRINT THAT NUM WITH FIZZ
IF DIVISABLE BY 5 PRINT THAT NUM WITH BUZZ
IF DIVISABLE BY 3 & 5 PRINT FIZZ BUZZ
'''
'''
#########################################
#VARS

fb = [
c := 0,
fizz := "fizz",
Buzz := "buzz",
m := 100,
]

#########################################
#REFACTOR


#########################################
#METHODS
#if(fbList[0]/3 ==  or (fbList[0]/5 == int):

while(fb[0] <= 100):
	if(fb[0] % 3, fb[0] % 5 == 0):
		print (str(fb[0]) + " " + fb[1] + fb[2]), #print number and fizzbuzz

	elif(fb[0] % 3 == 0):
		print (str(fb[0]) + " " +  fb[1]), #print number + fizz
	

	elif(fb[0] % 5 == 0):
		print (str(fb[0]) + " " + fb[2]), #print number + buzz

	else:
		print(fb[0])
	
	fb[0]+=1

'''
'''
#########################################
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
'''
#REFACTOR METHOD
'''
counts = [ 
fizzcount := 0,
buzzcount := 0,
fizzbuzzcount := 0,
]

for number in range(1000001):
	if (number % 3 == 0) and (number % 5 == 0):
		print(str(number) + " " + fb[1] + fb[2]),
		counts[2] += 1
	elif (number % 3 == 0):
		print(str(number) + " " + fb[1]),
		counts[0] += 1
	elif (number % 5 == 0):
		print(str(number) + " " + fb[2]),
		counts[1] += 1
	else:
		print(str(number)),
print ("__________________________")
print (fb[1] + "\t" + fb[2] + "\t" + fb[1] + fb[2]),
print(str("{:,}".format(counts[0])) + "\t" + str("{:,}".format(counts[1])) + "\t" + str("{:,}".format(counts[2])))
#########################################
'''
'''
#code never used
#############################################################
nl = {														#
"fizzbuzz": if (number % 3 == 0) and (number % 5 == 0):		#
				print(str(number) + " " + fb[1] + fb[2]),	#
"fizz": 	elif (number % 3 == 0):							#
				print(str(number) + " " + fb[1]),			#
"buzz":		elif (number % 5 == 0):							#
				print(str(number) + " " + fb[2]),			#
"rest":		print(str(number)),								#
}															#
for number in range(101):									#
															#
#############################################################
#code never used
'''
'''
#########################################
#Creating functions
#########################################

def nameit(first_name, last_name):	
#def is handler to define your own function
#nameit it is the function name
#in the brackets is the arguement
#arguement = pseudo variable
#when you call it later everything under
#under the function block is actioned once
# once the arguement is passed through
	#tabs are important
	#do something
	return("Hello " + first_name + " " + last_name)

#use a function
print(nameit("John", "Elder"))

#print(outcome * 20)

#print(mathit(9, 1)) #can't use function before defined

def mathit(num1, num2):
	return(num1 + num2)

#print(mathit(9, 1)) # math it directly handled

outcome = mathit(9,1) #mathit inderictely hadled by var

print(outcome * 20) # function var handled by var can be 
					# manipulated
'''
'''
#########################################
# Modules
#########################################
namer("John")

#task find a module and learn the ins and outs of it.
'''

#########################################
#SQLite database
#########################################
#establish connection to db
conn = sqlite3.connect('customer.db')
#create curson
csr =  conn.cursor()
#create table

csr.execute("""CREATE TABLE customer (
				first_name text,
				last_name text,
				email text
)""") #SQL structure query language

#csr.execute("INSERT INTO customer VALUES ('John','Elder','john@codemy.com')")


csr.execute("SELECT * FROM customer")
csr.fetchone()
csr.fetchmany(number)


direct way of accessing info
print(csr.fetchall()[0][0]) #pull tuple 0 item 0 from database.

indirect assign csr.fetchall to a variable

items = csr.fetchall()

#for loop to get database entries out of database

#for item in items:
#	print (item)

#for loop to get specific database column out of database

#for item in items:
#	print (item[0])

#for loop concatonated for multiple columns
for item in items:
	print(item[0] + " " + item[1])
#commit our changes
conn.commit()




#close db connection
conn.close()


#########################################
#Tkinter GUI
#########################################
root = Tk()
root.title('codemy.com - Learn to code!')
root.geometry("400x400")

def hello():
	hello_label = Label(root, text="Hello " + myTextbox.get())
	hello_label.pack()

myLabel = Label(root, text="Enter your first name:")
myLabel.pack()

myTextbox = Entry(root, width=30)
myTextbox.pack()

myButton = Button(root, text="Submit", command=hello)
myButton.pack()

root.mainloop()


