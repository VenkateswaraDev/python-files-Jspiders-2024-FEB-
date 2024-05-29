class Bank:
    bank_name = 'SBI'
    bank_ifsc = 12345
    bank_roi = 6
    bank_address = 'MYD'
    def __init__(self,n,ac,b,ad):
        self.name = n
        self.account = ac
        self.balance = b
        self.address = ad
        
c1 = Bank('Venky',7731,10000,'MYD')
c2 = Bank('amar',9981,20000,'HYD')

print(c1.name)
print(c2.name)