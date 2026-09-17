#Print Given number Plaindroem or Not Using Loop 
num = int(input("Enter Any Number : "))

print("Actual NUmber is : ",num)
temp = num
rev = 0
while(num != 0):
    rem = num % 10
    rev = rev*10 + rem
    num = num // 10

if rev == temp:
    print("Given number is Planidrome : ")
else:
    print("Given number is Not Planidrome : ")     
