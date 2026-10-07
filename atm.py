# ATM Simulation Program

balance = 1000.00
stored_pin = 1010


def user_login():
    print("Welcome to the ATM.")
    while True:
        try:
            entered_pin = int(input("Please enter your PIN: "))
        except ValueError:
            print("PIN must be a number. Please try again.")
            continue

        if entered_pin == stored_pin:
            print("Login successful.")
            break
        else:
            print("Incorrect PIN. Please try again.")


def check_balance():
    print(f"Your current balance is: €{balance:.2f}")


def withdraw():
    global balance
    try:
        amount = float(input("Enter the amount you wish to withdraw: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    if amount <= 0:
        print("Invalid amount. Please enter a value greater than zero.")
    elif amount > balance:
        print(f"Insufficient funds. Your balance is: €{balance:.2f}")
    else:
        balance = balance - amount
        print("Withdrawal successful.")
        print(f"Amount withdrawn: €{amount:.2f}")
        print(f"New balance: €{balance:.2f}")


def deposit():
    global balance
    try:
        amount = float(input("Enter the amount you wish to deposit: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    if amount <= 0:
        print("Invalid amount. Please enter a value greater than zero.")
    else:
        balance = balance + amount
        print("Deposit successful.")
        print(f"Amount deposited: €{amount:.2f}")
        print(f"New balance: €{balance:.2f}")


def main():
    user_login()

    while True:
        print("\nPlease select an option:")
        print("1 - Check Balance")
        print("2 - Withdraw")
        print("3 - Deposit")
        print("4 - Exit")

        choice = input("Choice: ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            withdraw()
        elif choice == "3":
            deposit()
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye.")
            break
        else:
            print("Invalid option. Please try again.")


main()
