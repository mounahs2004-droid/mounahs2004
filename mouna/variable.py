# simple calculator

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2 if num2 != 0 else "Undefined"

print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)


#Temperature converter

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32

print("Fahrenheit:", fahrenheit)

