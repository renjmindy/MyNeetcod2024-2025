from sortedcontainers import SortedDict

class Employee:
    def __init__(self, eid, role):
        self.eid = eid
        self.role = role
        
    def __lt__(self, other):
        return (self.eid, self.role) < (other.eid, other.role)
        
    def __gt__(self, other):
        return (self.eid, self.role) > (other.eid, other.role)
        
    def __eq__(self, other):
        return (self.eid, self.role) == (other.eid, other.role)

    def __ne__(self, other):
        return (self.eid, self.role) != (other.eid, other.role)

    def __hash__(self):
        return hash((self.eid, self.role))
        

employees = SortedDict()
employees[Employee(2, 'Developer')] = 'Alice'
employees[Employee(1, 'Manager')] = 'Bob'

# Intended to output the roles in order of employee ID, but there's an issue
for employee in employees:
    print(f'Employee ID: {employee.eid}, Role: {employee.role}, Name: {employees[employee]}')
