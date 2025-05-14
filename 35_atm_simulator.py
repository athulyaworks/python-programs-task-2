
balance = 1000.00  # Starting balance
pin = "1234"       # Default PIN
transaction_history = []

def show_welcome():
    """Show welcome message"""
    print("\n" + "="*50)
    print("        WELCOME TO SIMPLICITY BANK ATM")
    print("="*50)
    print("Your trusted banking partner")
    print("-"*50)

def authenticate():
    """Simple PIN authentication"""
    attempts = 3
    
    while attempts > 0:
        entered_pin = input(f"\nEnter your 4-digit PIN ({attempts} attempts remaining): ")
        
        if entered_pin == pin:
            print("✓ Authentication successful!")
            return True
        else:
            attempts -= 1
            if attempts > 0:
                print(f" Incorrect PIN. You have {attempts} attempts remaining.")
            else:
                print(" Too many incorrect attempts. Access denied!")
                print("Please contact your bank for assistance.")
    
    return False

def show_main_menu():
    """Display the main ATM menu"""
    print("\n" + "="*40)
    print("           MAIN MENU")
    print("="*40)
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transfer Money")
    print("5. Change PIN")
    print("6. View Transaction History")
    print("7. Exit")
    print("-"*40)

def check_balance():
    """Display current account balance"""
    print("\n" + "="*40)
    print("         ACCOUNT BALANCE")
    print("="*40)
    print(f"Current Balance: ${balance:.2f}")
    print("-"*40)
    transaction_history.append(f"Balance inquiry: ${balance:.2f}")

def deposit_money():
    """Handle money deposit"""
    global balance
    
    print("\n" + "="*40)
    print("         DEPOSIT MONEY")
    print("="*40)
    
    while True:
        try:
            amount = float(input("Enter deposit amount (or '0' to cancel): $"))
            
            if amount == 0:
                print("Deposit cancelled.")
                return
            elif amount < 0:
                print("Please enter a positive amount.")
            elif amount > 10000:
                print("Daily deposit limit is $10,000.")
            else:
                balance += amount
                print(f"\n✓ Deposit successful!")
                print(f"Deposited: ${amount:.2f}")
                print(f"New Balance: ${balance:.2f}")
                transaction_history.append(f"Deposit: +${amount:.2f}")
                return
        except ValueError:
            print("Please enter a valid amount.")

def withdraw_money():
    """Handle money withdrawal"""
    global balance
    
    print("\n" + "="*40)
    print("         WITHDRAW MONEY")
    print("="*40)
    print(f"Current Balance: ${balance:.2f}")
    
    while True:
        try:
            amount = float(input("Enter withdrawal amount (or '0' to cancel): $"))
            
            if amount == 0:
                print("Withdrawal cancelled.")
                return
            elif amount < 0:
                print("Please enter a positive amount.")
            elif amount > balance:
                print(f"Insufficient funds! Your balance is ${balance:.2f}")
            elif amount > 500:
                print("Daily withdrawal limit is $500.")
            else:
                balance -= amount
                print(f"\n✓ Withdrawal successful!")
                print(f"Withdrawn: ${amount:.2f}")
                print(f"New Balance: ${balance:.2f}")
                print("\nPlease take your cash.")
                transaction_history.append(f"Withdrawal: -${amount:.2f}")
                return
        except ValueError:
            print("Please enter a valid amount.")

def transfer_money():
    """Handle money transfer (simplified simulation)"""
    global balance
    
    print("\n" + "="*40)
    print("         TRANSFER MONEY")
    print("="*40)
    print(f"Current Balance: ${balance:.2f}")
    
    # Get recipient account (simplified)
    recipient = input("Enter recipient account number (or 'cancel'): ")
    if recipient.lower() == 'cancel':
        print("Transfer cancelled.")
        return
    
    while True:
        try:
            amount = float(input("Enter transfer amount: $"))
            
            if amount <= 0:
                print("Please enter a positive amount.")
            elif amount > balance:
                print(f"Insufficient funds! Your balance is ${balance:.2f}")
            elif amount > 1000:
                print("Daily transfer limit is $1,000.")
            else:
                # Simulate processing time
                print("\nProcessing transfer... Please wait.")
                
                balance -= amount
                print(f"\n✓ Transfer successful!")
                print(f"Transferred: ${amount:.2f}")
                print(f"To account: {recipient}")
                print(f"New Balance: ${balance:.2f}")
                transaction_history.append(f"Transfer: -${amount:.2f} to {recipient}")
                return
        except ValueError:
            print("Please enter a valid amount.")

def change_pin():
    """Change ATM PIN"""
    global pin
    
    print("\n" + "="*40)
    print("          CHANGE PIN")
    print("="*40)
    
    # Verify current PIN
    current_pin = input("Enter current PIN: ")
    if current_pin != pin:
        print("✗ Incorrect current PIN.")
        return
    
    # Get new PIN
    while True:
        new_pin = input("Enter new 4-digit PIN: ")
        
        if len(new_pin) != 4 or not new_pin.isdigit():
            print("PIN must be exactly 4 digits.")
            continue
        
        confirm_pin = input("Confirm new PIN: ")
        
        if new_pin == confirm_pin:
            pin = new_pin
            print("\n✓ PIN successfully changed!")
            transaction_history.append("PIN changed")
            return
        else:
            print("PINs don't match. Please try again.")

def view_transaction_history():
    """Display recent transactions"""
    print("\n" + "="*50)
    print("       TRANSACTION HISTORY")
    print("="*50)
    
    if not transaction_history:
        print("No transactions found.")
    else:
        # Show last 10 transactions
        recent_transactions = transaction_history[-10:]
        for i, transaction in enumerate(recent_transactions, 1):
            print(f"{i}. {transaction}")
    
    print("-"*50)

def main():
    """Main ATM application"""
    show_welcome()
    
    # Authentication
    if not authenticate():
        return
    
    print("\n✓ Welcome! What would you like to do today?")
    
    # Main menu loop
    while True:
        show_main_menu()
        
        try:
            choice = input("Select an option (1-7): ").strip()
            
            if choice == '1':
                check_balance()
            
            elif choice == '2':
                deposit_money()
            
            elif choice == '3':
                withdraw_money()
            
            elif choice == '4':
                transfer_money()
            
            elif choice == '5':
                change_pin()
            
            elif choice == '6':
                view_transaction_history()
            
            elif choice == '7':
                print("\n" + "="*40)
                print("Thank you for using Simplicity Bank ATM!")
                print("Have a great day! ")
                print("="*40)
                break
            
            else:
                print("\nInvalid selection. Please choose 1-7.")
        
        except KeyboardInterrupt:
            print("\n\nSession terminated. Have a great day!")
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            print("Please try again.")

# Run the ATM simulation
if __name__ == "__main__":
    main()