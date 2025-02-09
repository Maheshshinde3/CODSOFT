def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x // y  # Integer division
    else:
        return "Error! Division by zero."

def main():
    print("Simple Calculator")

    # for simplification i had used integer datatype. we can also perform them with float number by simply changing datatype to float
    try:
        num1 = int(input("Enter the first number : "))
        num2 = int(input("Enter the second number : "))
    except ValueError:
        print("Invalid input! Please enter integer values.")
        return

    # Display operation choices
    print("\nSelect the operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Prompt user to choose an operation
    choice = input("Enter the number corresponding to the operation: ")

    # Perform calculation based on user's choice
    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid choice! Please select a valid operation.")

if __name__ == "__main__":
    main()
