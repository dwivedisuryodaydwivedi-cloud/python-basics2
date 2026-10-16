""" 
*                 * 
* *             * * 
* * *         * * * 
* * * *     * * * * 
* * * * * * * * * * 
* * * * * * * * * * 
* * * *     * * * * 
* * *         * * * 
* *             * * 
*                 * 

"""
# Upper loop 
for i in range(1,6):
  for j in range(1,i+1):
    print("*",end=" ")
  for k in range(5,i,-1):
    print("  ",end="  ")
  for l in range(i,0,-1):
    print("*",end=" ")
  print()

# Lower loop 
for i in range(5,0,-1):
  for k in range(1,i+1):
    print("*",end=" ")
  for j in range(5,i,-1):
    print("  ",end="  ")
  for l in range(i,0,-1):
    print("*",end=" ")
  print()

