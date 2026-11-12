def check2(num):

  for i in range(2,num):
    if num%i == 0 :
      print("Not prime")
  else:
    print("Prime")
num = int(input("Enter your number :"))
check2(num)
