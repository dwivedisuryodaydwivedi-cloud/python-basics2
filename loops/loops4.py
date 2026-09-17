#Print Given number into reverse Order Using Loop 
num = int(input("Enter Any Number : "))

print("Actual NUmber is : ",num)
rev = 0
while(num != 0):
    rem = num % 10
    rev = rev*10 + rem
    num = num // 10

print("Prin Given number into Reverse Order : ",rev)     
