# serching  the given list of element using loop [1,4,9,16,25,36,49,64,81,100]
num = int(input("enter your number:"))
nums = [1,4,9,16,25,36,49,64,81,100]
for i in range(len(nums)): # loop for printing one to 10 number 
  if nums[i] == num: # This simply go step by step at every value  through  and whenever index found print that index value 
    print("Number found ",i)
  
