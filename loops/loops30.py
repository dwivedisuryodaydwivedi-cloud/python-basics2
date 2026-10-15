%%writefile loops30.py
"""
      * * * * * * * * * *
      * * * *     * * * *
      * * *         * * *
      * *             * *
      *                 *
      *                 *
      * *             * *
      * * *         * * *
      * * * *     * * * *
      * * * * * * * * * *

"""
for i in range(5,0,-1):
  for j in range(1,i+1,1):
    print(j,end=" ")
  for o in range(5,i,-1):
      print("  ",end="  ")
  for p in range(i,0,-1):
      print(p,end=" ")
  print()

for k in range(1,6,1):
 
  for l in range(1,k+1,1):
    print(l,end=" ")

  for o in range(5,k,-1):
       print("  ",end="  ")
  for p in range(k,0,-1):
    print(p,end=" ")
  print()
