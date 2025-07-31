#if condition
#To check leap year

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("It's a leap year.")
else:
    print("It's not a leap year.")

# if condition
#user authentication

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful!")
else:
    print("Invalid credentials.")

