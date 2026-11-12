# WAP FOR CHECKING THE GIVEN NUMBER IS EVEN OR ODD
def check(num):
  if num % 2 == 0 :
    return True
  else :
    return False
num = int(input("Enter your number : "))
answer = check(num)
if answer :
  print("Givne number is even ")
else :
  print("Given number is odd ")
