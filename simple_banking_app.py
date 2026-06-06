# ============================================================
# ARY Bank - Simple Banking System
# Description: A console-based banking application that allows
#              users to check balance, deposit, withdraw, and
#              manage KYC documents.
# ============================================================

# Global balance and KYC storage
balance = 0.0
kyc_document = {}


def check_balance():
    """Display the current account balance."""
    print("============================================")
    print(f"Your Current Balance is: ${balance:.2f}")
    print("============================================")


def deposit(amount):
    """
    Deposit a valid positive amount into the account.
    Updates global balance and returns True if successful, False otherwise.
    """
    global balance
    if amount > 0:
        balance += amount
        print(f"Successfully deposited ${amount:.2f}. New balance: ${balance:.2f}")
        return True
    else:
        print("Error: Cannot deposit an invalid amount (negative or zero)!")
        print("============================================")
        return False


def withdraw(amount):
    """
    Withdraw a valid amount from the account.
    Returns True if successful, False if invalid or insufficient funds.
    """
    global balance
    if amount <= 0:
        print("Error: Can't withdraw a negative or zero amount.")
        print("============================================")
        return False
    elif amount > balance:
        print("Error: Can't withdraw due to insufficient balance.")
        print("============================================")
        return False
    else:
        balance -= amount
        print(f"Successfully withdrew ${amount:.2f}. New balance: ${balance:.2f}")
        return True
        
        
def update_kyc(docs):
    """Update global KYC record with new documents."""
    global kyc_document 
    kyc_document.update(docs)
    
def check_kyc():
    """Display current KYC documents."""
    print("======================== KYC STATUS ========================")
    if len(kyc_document) == 0:  
        print("KYC status: Pending (No documents submitted)")
    else:    
        for doc, doc_id in kyc_document.items():
            print(f"{doc}: {doc_id}")           
    print("============================================================")


if __name__ == "__main__":
    print("============================================")
    print("        Welcome to ARY Bank!!               ")
    print("============================================")

    while True:
        print("\n1. Check your balance")
        print("2. Deposit an amount")
        print("3. Withdraw an amount")
        print("4. Check KYC documents")
        print("5. Update KYC documents")
        print("6. Quit")
        print("============================================================")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            check_balance()
            
        elif choice == '2':
            try:
                amt = float(input("Enter the amount to deposit: "))
                if deposit(amt):
                    print(f"Transaction Success: ${amt:.2f} credited successfully.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
                
        elif choice == '3':
            try:
                amt = float(input("Enter the amount to withdraw: "))
                if withdraw(amt):
                    print(f"Transaction Success: ${amt:.2f} debited successfully.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
                
        elif choice == '4':
            check_kyc()     
            
        elif choice == '5':
            kyc_docs = {}
            try:
                n_documents = int(input("Enter the number of documents you want to add:\n"))
                for i in range(n_documents):
                    key = input(f"Enter document type {i+1} (e.g., Passport, DL):\n").strip()
                    value = input(f"Enter {key} number:\n").strip()
                    if key and value:
                        kyc_docs[key] = value
                
                if kyc_docs:
                    update_kyc(kyc_docs)
                    print("KYC updated successfully!")
                else:
                    print("No documents were added.")
            except ValueError:
                print("Invalid input. Please enter a valid number for the document count.")               
        elif choice == '6':
            print("Quitting. Have a nice day!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
            print("============================================")

    print()
    print("Thank you for using ARY Bank services.")