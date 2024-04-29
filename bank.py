
class Bank:
    bankUser = []
    admin = []
    loan_amount = 0
    balance = 20000
    loan_feature = True
    def __init__(self) -> None:
        self.name = 'E-Bank'

    def add_user(self, user):
        if not self.bankUser :
            print("You don't have any user yet.")
        else:
            self.bankUser.append(user)

    def delete_users(self, name):
        for key in Bank.bankUser:
            if key.name == name:
                Bank.bankUser.remove(key)
                print("Removed User From This Bank ")
            else:
                print("User Not Found !!!")
            
    def all_users(self):
        for key in Bank.bankUser:
            print(f"Account Number is : {key.account_number}\nAccount Holder Name : {key.name}\nAccount Holder Email : {key.email}\nTotal balance : {key.balance}\n...............................")

    
    def admin_login(email, passwword ):
        for key in Bank.admin:
            if key.email == email and key.password == passwword :
                return key
            
            
    def user_login(email, passwword):
        for key in Bank.bankUser:
            if key.email == email and key.password == passwword :
                return key
            else:
                print("---------- User Not Found ---------")


