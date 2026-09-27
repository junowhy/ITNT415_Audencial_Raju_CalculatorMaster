def display_menu():
    print("\n===== Calculator Master =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

def get_numbers():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter numeric values.")

def main():
    while True:
        display_menu()
        choice = input("Select an option (1-5): ")

        if choice == "5":
            print("Exiting Calculator Master. Goodbye!")
            break
        elif choice == "1":
            num1, num2 = get_numbers()
            print(f"Result: {add(num1, num2)}")
        elif choice == "2":
            num1, num2 = get_numbers()
            print(f"Result: {subtract(num1, num2)}")
        elif choice in ("3", "4"):
            print("This operation is not yet implemented.")
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
    
def divide(a, b):
    """Return a divided by b, handling division by zero."""
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return a minus b."""
    return a - b

def multiply(a, b):
    """Return a multiplied by b."""
    return a * b
    
