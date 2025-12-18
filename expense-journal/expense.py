import json
from datetime import date
import os

#PATH

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TRANSACTION_FILE = os.path.join(BASE_DIR, "transactions.json")
ACCOUNT_FILE = os.path.join(BASE_DIR, "account.json")

#ACCOUNT

if os.path.exists(ACCOUNT_FILE):
    with open(ACCOUNT_FILE, "r") as f:
        account = json.load(f)
else:
    opening_balance = float(input("Enter your current account balance: "))
    account = {"opening_balance": opening_balance}
    with open(ACCOUNT_FILE, "w") as f:
        json.dump(account, f, indent=4)


if os.path.exists(TRANSACTION_FILE):
    with open(TRANSACTION_FILE, "r") as f:
        transactions = json.load(f)
else:
    transactions = []

#FUNCTIONS

def save_transactions():
    with open(TRANSACTION_FILE, "w") as f:
        json.dump(transactions, f, indent=4)

def calculate_balance():
    balance = account["opening_balance"]
    for t in transactions:
        if t["type"] == "credit":
            balance += t["amount"]
        else:
            balance -= t["amount"]
    return balance

def show_transactions():
    if not transactions:
        print("\nNo transactions found.")
        return

    for i, t in enumerate(transactions, start=1):
        print(
            f"\nTxn #{i} | {t['date']} | {t['type'].upper()} | "
            f"{t['category']} | ₹{t['amount']}"
        )
        print(f"Note: {t['note']}")

#MAIN MENU

while True:
    print("\n Menu ")
    print("1. Add Transaction")
    print("2. View All Transactions")
    print("3. Edit Transaction")
    print("4. Delete Transaction")
    print("5. Show Current Balance")
    print("6. Exit")

    choice = input("Choose an option: ")

    #ADD TRANSACTION
    if choice == "1":
        amount = float(input("Enter amount: "))

        type_ = input("Transaction type (credit/debit): ").lower()
        if type_ not in ("credit", "debit"):
            print("Invalid transaction type.")
            continue

        category = input("Category: ")
        note = input("Note: ")

        user_date = input("Date (press Enter for today): ")
        final_date = date.today().isoformat() if user_date == "" else user_date

        transaction = {
            "amount": amount,
            "type": type_,
            "category": category,
            "date": final_date,
            "note": note
        }

        transactions.append(transaction)
        save_transactions()
        print("Transaction added successfully.")

    #VIEW TRANSACTIONS
    elif choice == "2":
        show_transactions()

    #EDIT TRANSACTION
    elif choice == "3":
        show_transactions()
        if not transactions:
            continue

        index = int(input("\nEnter transaction number to edit: ")) - 1
        if index < 0 or index >= len(transactions):
            print("Invalid selection.")
            continue

        t = transactions[index]
        print("Press Enter to keep existing value.")

        new_amount = input(f"Amount ({t['amount']}): ")
        new_category = input(f"Category ({t['category']}): ")
        new_note = input(f"Note ({t['note']}): ")

        if new_amount:
            t["amount"] = float(new_amount)
        if new_category:
            t["category"] = new_category
        if new_note:
            t["note"] = new_note

        save_transactions()
        print("Transaction updated.")

    #DELETE TRANSACTION
    elif choice == "4":
        show_transactions()
        if not transactions:
            continue

        index = int(input("\nEnter transaction number to delete: ")) - 1
        if index < 0 or index >= len(transactions):
            print("Invalid selection.")
            continue

        deleted = transactions.pop(index)
        save_transactions()
        print(
            f"Deleted transaction: ₹{deleted['amount']} "
            f"({deleted['category']})"
        )

    #SHOW BALANCE
    elif choice == "5":
        print("Current Balance:", calculate_balance())

    #EXIT
    elif choice == "6":
        print("Goodbye.")
        break

    else:
        print("Invalid option. Choose 1-6.")
