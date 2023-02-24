import re

email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

email = input("Enter your Email: ")

if re.search(email_condition,email):
    print("Entered Email is Valid")
else:
    print("Invalid Email,Please correct your Email")