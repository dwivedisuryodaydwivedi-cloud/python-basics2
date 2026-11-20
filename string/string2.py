# Printing the reverse order of string :
name = "Guru dwivedi"
for i in range(len(name)-1,-1,-1): # this print the string into reverse order
  print(name[i],end="")
print()

# this is also used to print the string in reverse order
print(name[::-1])
