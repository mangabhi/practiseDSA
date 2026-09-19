class BankAccount:
    #method depoist withdrawl ,get_balance
    #create a constructor
    def __init__(self,account_number:int,customer_name:str):
        #private attributes
        self._account_number=account_number
        self._customer_name=customer_name
        self._balance:float=0

    def deposit(self,amount:float):
        if amount >0 :
            self._balance +=amount

    def withdraw(self,amount:float):
        if amount > 0:
            if amount > self._balance:
                print("Don't have Sufficient balance in your account")
                return 
            self._balance -=amount

    def get_balance(self):
        print (f"{self._customer_name} with Account Number {self._account_number} balance is {self._balance:.2f}")

b1=BankAccount(130012,"Abhishek")
b1.deposit(2000.98)
b1.deposit(700.76)
b1.get_balance()
b1.withdraw(400.01)
b1.get_balance()