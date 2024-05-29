class Bank:
    bank_name = 'SBI'
    bank_ifsc = 12345
    bank_roi = 6
    bank_address = 'MYD'
    
venky = Bank()
amar= Bank()

# Accessing the generic properties by using class

print(Bank.bank_name)

# Accessing the generic properties by using object

print(venky.bank_name)
print(amar.bank_name)

#Modifing of generic properties by using class

Bank.bank_roi = 5

print(Bank.bank_roi)
'''If we modify the generic properties by using class then it will change in class as well as objects'''
print(venky.bank_roi)
print(amar.bank_roi)



#Modifing of generic properties by using object

venky.bank_address = 'delhi'

print(Bank.bank_address)
print(venky.bank_address)
'''If we modify the generic properties by using object then it will change only that perticular object'''
print(amar.bank_address)


#Creating of new generic properties by using class

Bank.bank_code = 1001

print(Bank.bank_code)

'''If we create new generic properties by using class then it will create in class and in object'''
print(venky.bank_code)
print(amar.bank_code)

#Creating of new generic properties by using object
'''we can't create a new generic properties by using objects'''

