#class Employee:
#    def __init__(self, name, age, job_title, salary):
#        self.name = name
#        self.age = age
#        self.job_title = job_title
#        self.salary = salary
        
#    def display_employee_details(self):
#        print("Employee Details:")
#        print(f"Employee Name: {self.name}")
#        print(f"Employee Age: {self.age}")
#        print(f"Job Title: {self.job_title}")
#        print(f"Salary: {self.salary}")
 
class Personal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def display(self):
        print(f"Employee Name: {self.__name}")
        print(f"Employee Age: {self.__age}")
        
class Professional:
    def __init__(self, job_title, salary):
        self.__job_title = job_title
        self.__salary = salary
    def display(self):
        print(f"Job Title: {self.__job_title}")
        print(f"Salary: {self.__salary}")
        
class Employee:
    def __init__(self, name, age, job_title, salary):
        self.person = Personal(name, age)
        self.profession = Professional(job_title, salary) 
    def display(self):
        print("Employee Details:")
        self.person.display()
        self.profession.display()
        
# Example of using the combined single-class structure
emp1 = Employee("Alice", 30, "Engineer", 90000)
emp1.display()
