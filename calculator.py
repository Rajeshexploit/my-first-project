# Simple Calculator
print("Welcome to my calculator!")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

# Get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Select operation:")
print("1. Add")
print("2. Subtract")

choice = input("Enter choice (1/2): ")

if choice == '1':
    print("Result:", add(num1, num2))
elif choice == '2':
    print("Result:", subtract(num1, num2))
else:
    print("Invalid input")
