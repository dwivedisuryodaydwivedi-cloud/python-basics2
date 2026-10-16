"""     * *
      * * * *
    * * * * * *
  * * * * * * * *
* * * * * * * * * * 
* * * * * * * * * *
  * * * * * * * *
    * * * * * *
      * * * *
        * * 
 
    """
# Upper left and right pattern loop :

for i in range(1,6):
  for j in range(5,i,-1):
    print(" ",end=" ")
  for k in range(i,0,-1):
    print(k,end=" ")
  for k in range(1,i+1):
     print(k,end=" ")
  print()

# Lower for left and right pattern loop :
for i in range(5,0,-1):
  for j in range(5,i,-1):
    print(" ",end=" ")
  for k in range(i,0,-1):
    print(k,end=" ")
  for l in range(1,i+1,1):
    print(l,end=" ")
  print()
