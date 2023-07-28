#message = "Hello, World!"
#
#for char in message:
#    print(char)
#    print(cha)
#

while True:
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 5:
        print("Exiting the calculator...")
        break

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == 1:
        result = num1 + num2
        operation = "+"
    elif choice == 2:
        result = num1 - num2
        operation = "-"
    elif choice == 3:
        result = num1 * num2
        operation = "*"
    elif choice == 4:
        result = num1 / num2
        operation = "/"
    else:
        print("Invalid choice!")
        continue

    print(f"{num1} {operation} {num2} = {result}")