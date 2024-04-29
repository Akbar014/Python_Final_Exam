
from abc import ABC, abstractmethod
import random 
from bank import Bank

class User(ABC):
    def __init__(self, name, email, password, address, account_type ) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.password = password
    @abstractmethod
    def profile_info(self):
        raise NotImplementedError


class BankUser(User):
    def __init__(self, name, email, password, address, account_type) -> None:
        super().__init__(name, email, password, address, account_type)
        self.balance = 0
        self.account_number = self.generate_account_number()
        self.transactions = []
        self.loan_time = 0
        self.password = password
        Bank.bankUser.append(self)

    def profile_info(self):
        print("--- Account Information ---")
        print(f"--> Account Holder name : {self.name} \nAccount Number : {self.account_number}\nAccount Holder Email : {self.email}\nAccount type  : {self.account_type}\nYour current balance is : {self.balance}")
        print("--- ---- ---")
    def generate_account_number(self):
        return str("Account-") + str(random.randint(0,100))

    def deposit_money(self, amount):
        self.balance += amount
        Bank.balance += amount
        self.transactions.append({'type' : 'deposit', 'amount' : amount})

    def withdraw_money(self, amount):
        if self in Bank.bankUser:
            if amount > self.balance:
                print("----------------  Withdrawal amount exceeded ------------")
            else:
                if amount > Bank.balance:
                    print("  The Bank is Bankrupt")
                else: 
                    self.balance -= amount
                    Bank.balance -= amount
                    self.transactions.append({'type' : 'withdraw', 'amount' : amount})
                    print(f"--------- Withdrawal amount: {amount} from {self.account_number} successfull   --------------") 
                    
        else:
            print("-------User is deleted by admin ------------")

    def check_balance(self):
        print(f"----------  Your current balance is : {self.balance}  ----------------")

    def transfer_money(self, amount, account_number):
        is_account_exist = False
        for key in Bank.bankUser:
            if key.account_number == account_number:  
                is_account_exist = True
                if amount > self.balance or amount > self.balance:
                    print("------------ Transfer amount exceeded --------------")
                else:
                    self.balance -= amount
                    self.transactions.append({'type' : 'money transfer', 'amount' : amount})
                    print(f"---------------  Transfered amount: {amount} from {self.name} Account to {account_number} ----------------------") 
                    key.balance += amount
            
        if not is_account_exist:
            print("------------------ Account does not exist --------------")
        
    def take_loan(self, amount):
        if amount > Bank.balance  or Bank.loan_feature== False :
            print("-----------------  You can not able to take loan {amount} TK --------------------")
        else:
            if self.loan_time == 2 :
                print("---------- You take loan already two times --------")
            else:
                self.loan_time += 1
                self.balance += amount
                Bank.balance -= amount
                Bank.loan_amount += amount
                self.transactions.append({'type' : 'loan taken', 'amount' : amount})
                print(f"------------------  Loan {amount} TK is added with your main balance.------------------")
            


    def transaction_history(self): 
        for transaction in self.transactions:
            print(f" ----------------- Type: {transaction['type']}, Amount: {transaction['amount']} -----------------")

        print(f"-------------------  Your Current balance is : {self.balance} ------------------------")

        
class Admin(User):
    def __init__(self, name, email, password, address, account_type) -> None:
        super().__init__(name, email, password, address, account_type)
        Bank.admin.append(self)
        

    def see_all_users(self):
        Bank.all_users(self)

    def delete_users(self,name):
        Bank.delete_users(self,name)

    def check_total_balance_of_bank(self):
        print(f" ---------------Total balance of the bank is : {Bank.balance} ---------------")

    def check_total_loan_amount(self):
        print(f"------------------  Total loan amount of the bank is : {Bank.loan_amount} ------------------------")

    def loan_feature_status_change(self, status):
        if status == 1:
            Bank.loan_feature = True
        elif status == 2:
            Bank.loan_feature = False

    

    def profile_info(self):
        print(f"------------------  Account Holder name : {self.name}\nAccount Holder Email : {self.email}\nAccount type  : {self.account_type} -------------------")
 





