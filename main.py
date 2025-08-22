import json
from datetime import datetime

# File to store user data
DATA_FILE = "users.json"

# Load users from file or create default
def load_data():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "1234": {"name": "Nithin", "balance": 5000, "history": []},
            "5678": {"name": "Alex", "balance": 3000, "history": []}
        }

def save_data(users):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4, ensure_ascii=False)

def display_menu():
    print("\n===== ATM Menu =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction History")
    print("5. Export Statement")
    print("6. Exit")

def log_transaction(user, action, amount):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user["history"].append(f"{now} - {action} ₹{amount}")

def check_balance(user):
    print(f"Your balance is: ₹{user['balance']}")

def deposit(user):
    try:
        amount = int(input("Enter deposit amount: "))
        if amount > 0:
            user["balance"] += amount
            log_transaction(user, "Deposited", amount)
            print(f"₹{amount} deposited successfully.")
        else:
            print("Amount must be greater than 0.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def withdraw(user):
    try:
        amount = int(input("Enter withdrawal amount: "))
        if amount > 0:
            if amount <= user["balance"]:
                user["balance"] -= amount
                log_transaction(user, "Withdrew", amount)
                print(f"₹{amount} withdrawn successfully.")
            else:
                print("Insufficient balance.")
        else:
            print("Amount must be greater than 0.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def show_history(user):
    if not user["history"]:
        print("No transactions yet.")
    else:
        print("\nTransaction History:")
        for h in user["history"][-5:]:  # show last 5
            print("-", h)

def export_statement(user):
    filename = f"{user['name']}_statement.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write("==== Transaction Statement ====\n")
        f.write(f"Account Holder: {user['name']}\n")
        f.write(f"Current Balance: ₹{user['balance']}\n")
        f.write("===============================\n\n")
        for h in user["history"]:
            f.write(h + "\n")
    print(f"Statement exported to {filename}")

# ===== ATM START =====
users = load_data()
pin = input("Enter your 4-digit PIN: ")

if pin not in users:
    print("Invalid PIN. Exiting...")
else:
    user = users[pin]
    print(f"\nWelcome {user['name']}!")

    while True:
        display_menu()
        choice = input("Enter choice (1-6): ")

        if choice == "1":
            check_balance(user)
        elif choice == "2":
            deposit(user)
        elif choice == "3":
            withdraw(user)
        elif choice == "4":
            show_history(user)
        elif choice == "5":
            export_statement(user)
        elif choice == "6":
            save_data(users)
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please choose between 1-6.")
