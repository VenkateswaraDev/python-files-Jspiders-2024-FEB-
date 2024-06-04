class Bank:
    bank_name = 'SBI'
    bank_ifsc = 1234
    bank_roi = 6
    bank_address = 'MYD'
    
    def __init__(self,name,account,balance,address):
        self.name = name
        self.account = account
        self.balance = balance
        self.address = address
        
    @classmethod
    def bank_details(cls):
        print(f'Bank Name = {cls.bank_name}')
        print(f'Bank Ifsc = {cls.bank_ifsc}')
        print(f'Bank roi = {cls.bank_roi}')
        print(f'Bank address = {cls.bank_address}')
    
    @staticmethod
    def get_values():
        intValue = int(input('Enter int value = '))
        return intValue
    
    @classmethod
    def modify_roi(cls):
        new_roi = cls.get_values()
        cls.bank_roi = new_roi
        print(f'roi is modified to {cls.bank_roi}')
        
    def withdraw(self):
        amount = self.get_values()
        if self.balance >= amount:
            self.balance -= amount
            print('Withdrawal is successfull')
            print(f'Balance is {self.balance}')
        else:
            print('In-sufficient balance')
            print(f'Balance is {self.balance}')
    
    def customer_details(self):
        print(f'name = {self.name}')
        print(f'account number = {self.account}')
        print(f'balance = {self.balance}')
        print(f'address = {self.address}')
        

c1 = Bank('venky',123456789,10000,'mydukur')
c2 = Bank('amar',234567890,20000,'mydukuru')

c2.customer_details()
Bank.bank_details()
c1.customer_details()
Bank.modify_roi()
c1.withdraw()
