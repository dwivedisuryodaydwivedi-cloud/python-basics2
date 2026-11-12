print("Before Function Invoked : ")

def show():
    print("Show Function Invoked : ")

def wish():
    print("Wish Invoked : ")
    show()

show()
wish()
print("After Function Invoked : ")
print("End.....")
