# Simple Banking Program

def show_balance(balance):
    print("**********************")
    print(f"Your balance is £{balance:.2f}")
    print("**********************")


def deposit():
    try:
        deposit_amount=float(input("Enter deposit amount: "))

        if deposit_amount<0:
            print("**********************")
            print("Deposit cannot be a negative value.")
            print("**********************")
            return 0
        else:
            print("**********************")
            print(f'Your deposited amount is £{deposit_amount:.2f}')
            print("**********************")
            return deposit_amount

    except ValueError:
        print("**********************")
        print("Invalid input.")
        print("**********************")
        return 0

    except TypeError:
        print("**********************")
        print('Invalid entry.')
        print("**********************")
        return 0


def withdraw(balance):
    try:
        withdraw_amount=float(input("Enter amount you want to withdraw: "))
        if withdraw_amount > balance:
            print("**********************")
            print("Insufficient funds.")
            print("**********************")
            return 0
        elif withdraw_amount<0:
            print("**********************")
            print('You cannot withdraw amount less than 0.')
            print("**********************")
            return 0
        else:
            print("**********************")
            print(f"£{withdraw_amount:.2f} have been withdrawn from your account.")
            print("**********************")
            return withdraw_amount

    except ValueError:
        print("**********************")
        print("Invalid entry.")
        print("**********************")
        return 0

    except TypeError:
        print("*********************")
        print('Invalid entry.')
        print("**********************")
        return 0



def main():
    balance=0
    is_running = True

    while is_running:
        print("**********************")
        print("    Banking Program   ")
        print("**********************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("**********************")


        choice=input("Enter your choice (1-4):  ")
        print("**********************")
        if choice=='1':
            show_balance(balance)
        elif choice=='2':
            balance= balance + deposit()

        elif choice=='3':
            balance=balance - withdraw(balance)

        elif choice=='4':
            is_running=False
        else:
            print("**********************")
            print("Not a valid entry.")
            print("**********************")

    print("**********************")
    print("Happy Holidays; thank you for visiting.")
    print("**********************")

if __name__=='__main__':
    main()

