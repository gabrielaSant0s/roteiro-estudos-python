from re import T


class BankAccount:
    def __init__(self):
        self._balance = 0   
        self.is_open = bool

    def get_balance(self):
        if self.is_open:
            return self._balance
        else:
            raise ValueError("account not open")
        
    def open(self):
        if self.is_open != True:
            self.is_open = True
            return self.is_open
        else:
            raise ValueError("account already open")
            
    def deposit(self, amount):
        if self.is_open:
            self.negative_values(amount)
            self._balance += amount
            return self._balance
        else:
            raise ValueError("account not open")
        

    def withdraw(self, amount):     
        if self.is_open:
            self.negative_values(amount)
            if amount > self._balance:
                raise ValueError("amount must be less than balance")
            self._balance -= amount
            return self._balance
        else:
            raise ValueError("account not open")
    
    def close(self):
        if self.is_open == True:
            self.is_open = False
            self._balance = 0
            return self.is_open
        else:
            raise ValueError("account not open")

    def negative_values(self, amount):
        if amount < 0:
            raise ValueError("amount must be greater than 0")
    
# conta = BankAccount()
# # # print(conta)
# print(conta.open())
# print(conta.deposit(10))

# print(conta.close())
# # # print(conta.withdraw(5))
# print(conta.open())
# print(conta.get_balance())

# print(conta)


