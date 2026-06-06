# Simple-banking-System


# 🏦 ARY Bank — Simple Banking System

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Platform](https://img.shields.io/badge/Platform-Console%20%2F%20Terminal-lightgrey)

A simple console-based banking system built in Python. It allows users to check their balance, deposit money, withdraw money, and submit KYC documents — all from the terminal.

---

## 📋 Table of Contents

- [About](#about)
- [Language & Tools](#language--tools)
- [Features](#features)
- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Code Concepts Used](#code-concepts-used)
- [Known Limitations](#known-limitations)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## About

ARY Bank is a beginner-level Python project that simulates a basic banking system on the command line. It was built to practice core Python concepts like functions, loops, global variables, dictionaries, and input validation.

There is no database or UI — everything runs in the terminal and resets when the program closes.

---

## Language & Tools

| Item | Detail |
|---|---|
| **Language** | Python 3.x |
| **Interface** | Command Line / Terminal |
| **IDE** | Any (VS Code, PyCharm, IDLE) |
| **Libraries** | None (uses Python built-ins only) |
| **Platform** | Windows, macOS, Linux |

No external libraries or installations are required beyond Python itself.

---

## Features

- ✅ Check current account balance
- ✅ Deposit money with validation
- ✅ Withdraw money with overdraft protection
- ✅ Submit KYC documents (stored as key-value pairs)
- ✅ Input validation (rejects negative amounts, invalid inputs)
- ✅ Error handling (prevents crashes on bad input)
- ✅ Clean exit with thank-you message

---


Usage
When you run the program, you will see:
===============================
 Welcome to ==>
 ARY Bank!!
===============================

1. Check your balance
2. Deposit an amount
3. Withdraw an amount
4. Submit KYC documents
5. Quit

Enter your choice (1-5):
Example — Deposit
Enter your choice (1-5): 2
Enter the amount to deposit: 5000
Successfully deposited 5000.00. New balance: 5000.00
Example — Withdraw
Enter your choice (1-5): 3
Enter the amount to withdraw: 1000
Successfully withdrew 1000.00. New balance: 4000.00
Example — Overdraft Protection
Enter your choice (1-5): 3
Enter the amount to withdraw: 99999
Can't withdraw due to insufficient balance.
Example — KYC
Enter your choice (1-5): 4
Enter the number of documents: 2
Enter document type 1: Passport
Enter document number 1: AB1234567
Enter document type 2: National ID
Enter document number 2: 42101-1234567-1
KYC updated successfully!
## How It Works

The program runs in an infinite loop and shows a menu to the user. Based on the user's choice, it calls the relevant function. The loop only breaks when the user selects **Quit**.

```
Program Starts
      │
      ▼
Display Menu (1-5)
      │
      ├── 1 → check_balance()   → prints current balance
      ├── 2 → deposit()         → adds amount to balance
      ├── 3 → withdraw()        → deducts amount from balance
      ├── 4 → update_kyc()      → stores document info in dictionary
      └── 5 → Quit              → breaks loop, exits program
```

The `balance` variable is global — all functions read from and write to the same variable.

---

## Project Structure

```
ary-bank/
│
├── banking.py       # Main program file
└── README.md        # Project documentation
```

Single-file project. All logic lives in `banking.py`.

---

## Getting Started

### Requirements

- Python 3.x installed on your machine
- A terminal or command prompt

### Check Python version

```bash
python --version
```

### Run the program

```bash
python banking.py
```

---

## Usage

When you run the program, you will see:

```
===============================
 Welcome to ==>
 ARY Bank!!
===============================

1. Check your balance
2. Deposit an amount
3. Withdraw an amount
4. Submit KYC documents
5. Quit

Enter your choice (1-5):
```

### Example — Deposit

```
Enter your choice (1-5): 2
Enter the amount to deposit: 5000
Successfully deposited 5000.00. New balance: 5000.00
```

### Example — Withdraw

```
Enter your choice (1-5): 3
Enter the amount to withdraw: 1000
Successfully withdrew 1000.00. New balance: 4000.00
```

### Example — Overdraft Protection

```
Enter your choice (1-5): 3
Enter the amount to withdraw: 99999
Can't withdraw due to insufficient balance.
```

### Example — KYC

```
Enter your choice (1-5): 4
Enter the number of documents: 2
Enter document type 1: Passport
Enter document number 1: AB1234567
Enter document type 2: National ID
Enter document number 2: 42101-1234567-1
KYC updated successfully!
```

---

## Code Concepts Used

| Concept | Where It Is Used |
|---|---|
| **Functions** | `check_balance()`, `deposit()`, `withdraw()`, `update_kyc()` |
| **Global Variables** | `balance` shared across all functions |
| **While Loop** | Infinite menu loop |
| **If / Elif / Else** | Menu choice handling and input validation |
| **Dictionary** | KYC documents stored as `{doc_type: doc_number}` |
| **For Loop** | Iterating over number of KYC documents |
| **f-strings** | Formatted output messages |
| **try / except** | Handles invalid (non-numeric) user input |
| **`__name__ == "__main__"`** | Standard Python entry point guard |
| **`input()`** | Reading user input from terminal |
| **`float()`** | Converting string input to decimal number |
| **`int()`** | Converting string input to integer (KYC count) |

---

## Known Limitations

- **No data persistence** — balance resets to `0.0` every time the program restarts
- **Single user only** — no login, accounts, or user profiles
- **No database** — KYC documents are lost when program closes
- **No transaction history** — past deposits and withdrawals are not recorded
- **Terminal only** — no graphical interface

---

## Future Improvements

- [ ] Add file or database storage to save balance between sessions
- [ ] Support multiple user accounts with login
- [ ] Add transaction history log
- [ ] Build a simple GUI using `tkinter`
- [ ] Add PIN or password protection
- [ ] Export account statement as a `.txt` or `.csv` file

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

> Built with Python 🐍 | ARY Bank — Learning Project
