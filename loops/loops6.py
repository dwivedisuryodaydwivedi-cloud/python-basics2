# Print Given number Armstrong or Not Using Loop 
num = int(input("Enter Any Number : "))
print("Actual NUmber is : ",num)

count = 0
temp = num
sum = 0

while(num !=0):
    num = num  // 10
    count = count + 1 
  
num = temp
while(num != 0):
    rem = num % 10
    sum = sum + (rem**count)
    num = num // 10

if sum == temp:
    print("Given number is Armstrong : ")
else:
    print("Given number is Not Armstrong : ")     
