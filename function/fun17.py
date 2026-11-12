from os import register_at_fork
x = int(input("Enter your number :"))
y = int(input("Enter your number :"))

result = 1
for i in range(y):
  result = result * x
print(result)
