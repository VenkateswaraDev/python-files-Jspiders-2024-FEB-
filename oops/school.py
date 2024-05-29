class School:
    school_name = 'DAV'
    school_address = 'RTPP'
    school_princaple = 'Venkateswara'
    def __init__(self,name,age,parentName,contact):
        self.name = name
        self.age = age
        self.parentName = parentName
        self.contact = contact
        
student_1 = School('Ravi',10,'Raj',9876543210)
student_2 = School('nani',11,'Dhoni',7789836251)
print(student_1.contact)
print(student_2.contact)