# WAP for prime number using for loop 
num  = int(input("Enter your number is :"))

for i in range(2,num):
  if num % i == 0 :
    print("not prime")
  
  else:
    print("prime")
    break
