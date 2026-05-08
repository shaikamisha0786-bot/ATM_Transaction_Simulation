#ATM Transaction Simulation
balance=1000.0


while True:
    print("\n ATM MENU")
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Check Balance")
    print("4.Exit")

    choice=int(input("Enter your choice:"))


    if choice == 1:
        amount=float(input("Enter deposit amount:"))
        if amount<=0:
            print("Invalid amount! Try again.")
            continue
        balance += amount
        print("Amount Deposited Successfully")


    elif choice == 2:
        amount=float(input("Enter Withdrawal amount:"))
        if amount > balance:
            print("Insufficient balance")
            continue
        balance -=amount
        print("Withdrawal Successful.")


    elif choice == 3:
        print("your current balance is:",balance) 

    elif choice == 4:
        print("Exiting ATM,Thank you!")
        break
    else:
        print("Invalid choice,Try again.")       