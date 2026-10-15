"""
      *
     **
    ***
   ****
  *****
  *****
   ****
    ***
     **
      *"""
for i in range(1,6,1):
  for j in range(5,i,-1):
    print(" ",end="")
  for k in range(1,i+1,1):
    print("*",end="")
  print()
for l in range(5,0,-1):
  for m in range(5,l,-1):
    print(" ",end="")
  for n in range(l,0,-1):
    print("*",end="")
  print()
