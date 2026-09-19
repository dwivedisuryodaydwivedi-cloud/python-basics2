# WAP to find the fectorial of any number 

n = int(input("enter your number n :"))
fact = 1
for i in range(n,0,-1):
  fact = fact*i
print(fact)
