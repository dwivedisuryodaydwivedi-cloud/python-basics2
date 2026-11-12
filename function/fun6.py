# program for creating user login using function :
def login():
  username = input("Enter your username :")
  password = int(input("Enter your password :"))

  if username == "Suryoday"  and password == 12345 :
    print("student login successfully")
  elif username == "admin" and password == 12345 :
    print("admin login succesfully")
  elif username == "Teacher" and password == 12345 :
    print("teacher login succesfully")
  else :
    print("Invalid username or password")
login()
