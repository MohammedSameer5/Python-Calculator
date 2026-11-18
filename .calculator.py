num1 = int(input("Enter first number: "))
op = input("Enter operation: ")
num2 = int(input("Enter second number: "))

if op == "+":
    print("The result:", num1 + num2)

elif op == "-":
    print("The result:", num1 - num2)

elif op == "*":
    print("The result:", num1 * num2)

elif op == "/":
    print("The result:", num1 / num2)

else:
    print("Invalid operation")