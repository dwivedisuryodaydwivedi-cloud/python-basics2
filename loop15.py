# printing the sum of first n number using loop

n = int(input("enter your number n:"))
sum = 0 # stores the curent value based on iteration 
for i in range(1,n+1):
  sum = sum + i
print(sum)
