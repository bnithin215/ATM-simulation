def display_menu():
    print("\n===== ATM Menu =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction History")
    print("5. Exit")

def check_balance(balance):
    print(f"Your balance is: ₹{balance}")

def deposit(balance, history):
    try:
        amount = int(input("Enter deposit amount: "))
        if amount > 0:
            balance += amount
            history.append(f"Deposited ₹{amount}")
            print(f"₹{amount} deposited successfully.")
        else:
            print("Amount must be greater than 0.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    return balance

def withdraw(balance, history):
    try:
        amount = int(input("Enter withdrawal amount: "))
        if amount > 0:
            if amount <= balance:
                balance -= amount
                history.append(f"Withdrew ₹{amount}")
                print(f"₹{amount} withdrawn successfully.")
            else:
                print("Insufficient balance.")
        else:
            print("Amount must be greater than 0.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    return balance

def show_history(history):
    if not history:
        print("No transactions yet.")
    else:
        print("\nTransaction History:")
        for h in history:
            print("-", h)

# ATM starts here
balance = 5000
history = []

# Simple PIN authentication
pin = "1234"
entered_pin = input("Enter your 4-digit PIN: ")

if entered_pin != pin:
    print("Invalid PIN. Exiting...")
else:
    while True:
        display_menu()
        choice = input("Enter choice (1-5): ")

        if choice == "1":
            check_balance(balance)
        elif choice == "2":
            balance = deposit(balance, history)
        elif choice == "3":
            balance = withdraw(balance, history)
        elif choice == "4":
            show_history(history)
        elif choice == "5":
            confirm = input("Are you sure you want to exit? (y/n): ").lower()
            if confirm == "y":
                print("Thank you for using the ATM. Goodbye!")
                break
        else:
            print("Invalid option. Please choose between 1-5.")
