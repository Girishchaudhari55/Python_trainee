class Account:
    def __init__(self, number, name, minimum_bal = 1000):
        self.__number = number
        self.__name = name
        self.__balance = minimum_bal

    def __repr__(self):
        return f'[number = {self.__number}, name = {self.__name}, balance={self.__balance}]'
    
    def __str__(self):
        return self.__repr__()
    
    def deposit(self,amount):
        self.__balance+=amount
    
    def withdraw(self,amount):
        if amount >self.__balance:
         print('no enough balance')
        self.__balance-=amount
    
Rohit_ac = Account(name='Rohit',number='9996667779991', minimum_bal=10000)
print(Rohit_ac)

Rohit_ac.deposit(1)
print(Rohit_ac)

Rohit_ac.withdraw(2000)
print(Rohit_ac)
