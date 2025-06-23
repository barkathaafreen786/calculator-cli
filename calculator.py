

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

def display_menu():
    print("\n" + "=" * 30)
    print("🧮 Calculator CLI App")
    print("=" * 30)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

def main():
    print("🎉 Welcome to the Calculator CLI App!")
    
    while True:
        display_menu()
        choice = input("👉 Enter your choice (1-5): ").strip()

        if choice == '5':
            print("👋 Exiting the calculator. Goodbye!")
            break

        if choice not in ['1', '2', '3', '4']:
            print("❌ Invalid choice. Please try again.")
            continue

        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        if choice == '1':
            result = add(num1, num2)
            symbol = '+'
        elif choice == '2':
            result = subtract(num1, num2)
            symbol = '-'
        elif choice == '3':
            result = multiply(num1, num2)
            symbol = '*'
        elif choice == '4':
            result = divide(num1, num2)
            symbol = '/'
            if isinstance(result, str):
                print(f"❌ {result}")
                continue

        print(f"✅ Result: {num1} {symbol} {num2} = {result}")

if __name__ == "__main__":
    main()
