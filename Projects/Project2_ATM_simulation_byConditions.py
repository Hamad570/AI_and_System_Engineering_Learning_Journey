balance=5000
pin=1234

print('==============================')
print('| welcome to the ATM Machine.|' )
print('===============================')

emtered_pin=int(input("Enter your Pin code: "))
if emtered_pin==pin:
    print("Verification successful welcome to the process.")
    while True:
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        choice=input("\n please enter a number which you want to process: ")
        if choice=='1':
          print(f'The total Balance in you account is {balance}')
        elif choice=='2':
            am=int(input("Enter amount you want to deposit: "))
            if am<=0: print("Enter a valid amount please: ")
            else: 
                balance+=am
                print(f"The transaction is succefull of amount {am} \n New balance is {balance}")
        elif choice=='3':
            wd=int(input('Enter the Amount you want to withdraw: '))
            if wd<=0: print("Enter a valid amount please. ")
            elif wd>balance: print("Invalid Amount! ...Insufficient Balance.")
            else: 
                balance-=wd
                print(f"The transaction is succefull of amount {wd} \nNew balance is {balance}")
        elif choice=='4':
            print("\nThank you for using our ATM. Have a great day! ")
            break
        else: print("Please Enter a valid choice. ThankYou")
else: print("Invalid Pin Try again.Access Denied")