class Pg:
    pg_name = 'SLV boys pg'
    pg_rent = 6000
    pg_advance = 1000
    pg_contact = 7731849145
    pg_address = 'Delhi'
    
    def __init__(self,name,contact,proof,joinDate,rentStatus):
        self.name = name
        self.contact = contact
        self.proof = proof
        self.joinDate = joinDate
        self.rentStatus = rentStatus
        
person_1 = Pg('Venky',7731849145,'aadhar','01-01-2024','paid')
person_2 = Pg('Amar',9491696271,'aadhar','20-04-2024','un-paid')

print(f'name = {person_1.name} , JoinDate = {person_1.joinDate}, rent = {person_1.rentStatus}')
print(f'name = {person_2.name} ,JoinDate = {person_2.joinDate}, rent = {person_2.rentStatus}')