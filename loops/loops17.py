# WAP to find the fectorial of any number using for and while loop

num = int(input("enter your number n :"))
for i in range(2,num,1):
 if num%i==0:
  print("not prime")
  break

else:
  print("prime ")

# while loop
num = int(input("enter your number n :"))
p = 2
while i < num:
  if num%i==0:
    print("not prime")
    break
  i = i+1
if i == num:
  print("prime")

