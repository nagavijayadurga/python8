# ==========================================
# 1. Compare Two Integers
# ==========================================

a=10
b=20
if a > b:
    print ("a is larger than b")
elif b > a:
    print ("b is larger than a")
else:
    print ("Both numbers are equal")

# ==========================================
# 2. Logical Operators
# ==========================================

# Check if a number is between 10 and 20
number = int(input("Enter a number: "))

if 10 <= number <= 20:
    print("Number is within the range.")
else:
    print("Number is outside the range.")

# Check if a string is not empty and has more than 5 characters
text = input("Enter a string: ")

if len(text) > 5:
    print("Valid string.")
else:
    print("Invalid string.")


# ==========================================
# 3. Simple Calculator
# ==========================================

# Simple Calculator

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

if op == "+":
    result = num1 + num2

elif op == "-":
    result = num1 - num2

elif op == "*":
    result = num1 * num2

elif op == "/" and num2 != 0:
    result = num1 / num2

else:
    result = "Invalid operation or division by zero"

print("Result:", result)


# ==========================================
# 4. Age Classification
# ==========================================

# Age Classification

age = int(input("Enter your age: "))

if age < 13:
    print("Child")

elif age < 20:
    print("Teenager")

elif age < 60:
    print("Adult")

else:
    print("Senior")


# ==========================================
# 5. Simple Login System
# ==========================================

print("\nLogin System")

# Hardcoded credentials
correct_username = "admin"
correct_password = "password123"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Login Successful!")
else:
    print("Invalid Username or Password.")