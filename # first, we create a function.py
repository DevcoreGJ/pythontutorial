# first, we create a function
def switch(case):
 
  # check if the argument matches the cases
  if case == "celeron":
  print ("Forget about it and play Minesweeper instead...")
 
  elif case =="core i3":
  print ("Good luck with that ;)")
 
  elif case == "core i5":
  print ("Yeah, you should be fine.")
 
  elif case == "core i7":
  print ("Have fun!")
 
  elif case == "core i9":
  print ("Our teams designed nice loading screens... too bad you won't see them...")
 
  else:
  print ("Is that even a thing?")
 
# ask for the user input
cpuModel = str.lower(input("Please enter your CPU model: "))
 
# call the function
switch(cpuModel)