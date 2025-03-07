def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid numerical value.")

def display_menu():
    print("\nSimple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("q. Quit")

def main():
    operations = {
        '1': add,
        '2': subtract,
        '3': multiply,
        '4': divide
    }
    
    while True:
        display_menu()
        
        choice = input("Enter the operation number (1/2/3/4) or 'q' to quit: ").strip().lower()
        
        if choice == 'q':
            print("Goodbye!")
            break
        
        if choice in operations:
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")
            
            result = operations[choice](num1, num2)
            print(f"Result: {num1} {['+', '-', '*', '/'][int(choice)-1]} {num2} = {result}")
        else:
            print("Invalid choice! Please select a valid operation.")

if __name__ == "__main__":
    main()
