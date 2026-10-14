"""  5 4 3 2 1
       4 3 2 1
         3 2 1
           2 1
             1
                """
for i in range(5,0,-1): # this loop gives the numbers from 5 to 1

  for j in range(5,i,-1): # this loop gives the space between them in each columns 
    print("",end="  ")
  
  for k in  range(i,0,-1): # this loop decreases numbers from i as 5,4,3,2,1
    print(k,end=" ")
  
  print()
