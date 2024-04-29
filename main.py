from users import *
from bank import Bank

def user_option():
    name = input("Enter Your name : ")
    email = input("Enter your email : ")
    password = input("Enter your password : ")
    address = input("Enter your address : ")
    print("Account Type : ")
    print("1. Savings Account")
    print("2. Current Account")
    type = int(input("Press 1 for savings account , Press 2 for current account - "))
    if (type == 1):
        account_type = 'Savings'
    elif (type == 2):
        account_type = 'Current'

    user = BankUser(name=name, email=email, password=password, address=address, account_type=account_type)
    user.profile_info()



def admin_option():
    name = input("Enter Your name : ")
    email = input("Enter your email : ")
    password = input("Enter your password : ")
    address = input("Enter your address : ")
    account_type = 'admin'
    admin = Admin(name=name, email=email, password=password, address=address, account_type=account_type )
    admin.profile_info()


while True:
    print("1. Create Customer Account ")
    print("2. Login as Customer ")
    print("3. Create Admin Account ")
    print("4. Login as Admin ")
    print("5. Exit ")
    choice = int(input("Enter your choice here : "))
    if choice == 1:
        user_option()
        print("---Account Created Successfully !! Please login as User ---")
    elif choice == 2:
        email = input("Enter your email : ")
        password = input("Enter your password : ")
        user = Bank.user_login(email=email, passwword=password)
        if user:
            print("------------ 😊😊 Successfully Logged In as Customer😊😊 !!! ---------------")
            while True:
                print("-----------------Enter option to get our services.........................")
                print("1. Deposit Money ")
                print("2. Withdraw Money ")
                print("3. Check Available Balance ")
                print("4. Check Transaction History ")
                print("5. Take Loan ")
                print("6. Transfer Amount ")
                print("7. Exit ")

                choice = int (input("Enter your option here: "))
                if choice == 1:
                    amount = int(input("Enter Amount : "))
                    user.deposit_money(amount)
                    user.check_balance()
                elif choice== 2:
                    amount = int(input("Enter Amount : "))
                    user.withdraw_money(amount)
                elif choice == 3:
                    user.check_balance()
                elif choice == 4 :
                    user.transaction_history()
                elif choice == 5 :
                    amount = int(input("Enter Amount : "))
                    user.take_loan(amount)
                elif choice ==6 :
                    account_number = input("Receiver Account No : ")
                    amount = int(input("Enter Amount : "))
                    user.transfer_money(amount, account_number)
                elif choice == 7:
                    break
                else:
                    print("------ Invalid input !!!")
        else:
            print("--- Login Failed !!! Please try again ---")

    elif choice == 3 :
        admin_option()
        print("--- Account Created Successfully !! Please login as admin ---")
    elif choice == 4:
        email = input("Enter your email : ")
        password = input("Enter your password : ")
        admin = Bank.admin_login(email=email, passwword=password)
        if admin:
            print("------- 😊😊 Successfully logged In as Admin. 😊😊 ---------------")
            while True:
                print("1. Create Admin Account ")
                print("2. See All Bank User ")
                print("3. Delete User ")
                print("4. Check Total Balance Of The Bank ")
                print("5. Check Total Loan Amount Of The Bank ")
                print("6. Loan Feature Status Change ")
                print("7. Exit ")

                choice = int(input("Enter your choice here "))

                if choice == 1:
                    admin_option()
                elif choice == 2:
                    admin.see_all_users()
                elif choice== 3:
                    deleted_user = input("Enter user name : ")
                    admin.delete_users(deleted_user)
                elif choice == 4:
                    admin.check_total_balance_of_bank()
                elif choice == 5 :
                    admin.check_total_loan_amount()
                elif choice == 6:
                    print("1. Bank loan feature on")
                    print("2. Bank Loan feature off")
                    status = int(input("Enter 1 for on and 2 for off loan features "))
                    admin.loan_feature_status_change(status)
                elif choice ==7:
                    break
                else:
                    print("Invalid input !!! Please try again --------------")

        else:
            print("Login Failed !!! Please try again later.")
         
    elif choice == 5 :
        break
        
    else:
        print("Invalid input !!! Please try again -----------")





    
