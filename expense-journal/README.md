# Expense /Transaction Tracker (Python)

A menu-driven **console-based ledger application** built using Python.  
This project tracks **credits and debits**, maintains an **opening balance**, and calculates the **current balance dynamically** using persistent JSON storage.

Unlike basic expense trackers, this project follows **real-world accounting principles**.

---

# Features

###  Account Setup
- Prompts user for **opening balance** on first run
- Stores opening balance separately from transactions
- Ensures accurate balance calculations

###  Transaction Management (CRUD)
- **Add Transaction**
  - Supports both `credit` (income) and `debit` (expense)
  - Records amount, category, date, and note
- **View All Transactions**
  - Displays transactions in a clean ledger format
- **Edit Transaction**
  - Modify existing transaction details
- **Delete Transaction**
  - Safely remove a transaction

### 🔹 Balance Calculation
- Balance is calculated dynamically using:
- Balance is never stored directly

### 🔹 Persistent Storage
- Uses JSON files for data persistence
- Data is retained across program restarts

---

## 🧠 Concepts Practiced

- Python data structures (lists, dictionaries)
- Functions and control flow
- File handling with JSON
- Menu-driven program design
- Input validation
- Separation of concerns
- Real-world financial logic

---

## 📁 Project Structure

> `account.json` and `transactions.json` are generated at runtime and should not be committed.

---

## ⚙️ How to Run

1. Clone the repository
2. Navigate to the project directory
3. Run:
   ```bash
   python3 ledger.py
