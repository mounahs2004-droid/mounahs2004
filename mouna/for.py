#For loop
#print pattern(star traingle)

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
     print("*" * i)

# To count even or odd in a list

numbers = [1, 4, 7, 10, 13, 16, 19, 22]
even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
