""" 
1                 1 
1 2             2 1 
1 2 3         3 2 1 
1 2 3 4     4 3 2 1 
1 2 3 4 5 5 4 3 2 1 
1 2 3 4 5 5 4 3 2 1 
1 2 3 4     4 3 2 1 
1 2 3         3 2 1 
1 2             2 1 
1                 1 """

# Upper loop 
for i in range(1,6):
  for j in range(1,i+1):
    print(j,end=" ")
  for k in range(5,i,-1):
    print("  ",end="  ")
  for l in range(i,0,-1):
    print(l,end=" ")
  print()

# Lower loop 
for i in range(5,0,-1):
  for k in range(1,i+1):
    print(k,end=" ")
  for j in range(5,i,-1):
    print("  ",end="  ")
  for l in range(i,0,-1):
    print(l,end=" ")
  print()
