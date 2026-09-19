# wap to print the power of x to the power of y by using loop without using exponet function

x = int(input("Enter your number x :"))
y = int(input("Enter your number y :"))

power = 1
for i in range(1,y+1):
  power = power * x
print("x to the power y is "power)
