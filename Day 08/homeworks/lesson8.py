# Input customer's name and password
customer_name = input("Enter your name: ")
password = input("Enter your password: ")

# Repeat the password for confirmation
repeat_password = input("Repeat your password: ")

# Check if the passwords match
if password == repeat_password:
    print("You have successfully registered!")
else:
    print("Password is incorrect. Please try again.")