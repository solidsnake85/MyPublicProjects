# handle exception if age is invalid
try:
    age = int(input("Age "))
    if age >= 21:
        print("Legal to purchase")
except ValueError:
    print("Please enter a valid age")
    print("Program continues")  # message to user
else:
    if age < 21:
        print("Not legal")
