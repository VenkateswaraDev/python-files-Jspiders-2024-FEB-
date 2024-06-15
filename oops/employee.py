class Employee:
    CName = 'Google'
    Caddress = 'Bangalore'
    employee_count = 0
    
    def __init__(self,ename,eid,esalary):
        self.ename = ename
        self.id = eid
        self.esalary = esalary
        Employee.employee_count +=1
    
    def __del__(self):
        print('Employee resigned............!')
        Employee.employee_count -=1
        
        
emp1 = Employee('venky',123,10000)
emp2 = Employee('amar',234,20000)
print(f'Employee count = {Employee.employee_count}')
del emp2
print(f'Employee count = {Employee.employee_count}')
