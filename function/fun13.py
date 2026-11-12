# maiking program for calculating factorial for given input number
def fact(num):
  fact = 1
  if num >= 0 :
    for i in range(1,num+1):
      fact = fact * i
    return fact
  else :
    return "invalid number for fact"

num = int(input("Enter your number :"))
answer = fact(num)
print(answer)
