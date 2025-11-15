import copy
import math

def salary_increment(employees):
    # implement this
    # pass
    for employee in employees:
        if employee['role'] == 'developer': employee['salary'] = math.ceil(employee['salary'] * 1.15)
        
    return employees

# Test cases

employees = [{
    'name': 'John',
    'role': 'developer',
    'salary': 50000
}, {
    'name': 'Mary',
    'role': 'developer',
    'salary': 70000
}, {
    'name': 'Jim',
    'role': 'manager',
    'salary': 85000
}]

print(salary_increment(employees))
# Expected output: [{'name': 'John', 'role': 'developer', 'salary': 57500}, 
#                   {'name': 'Mary', 'role': 'developer', 'salary': 80500.0},
#                   {'name': 'Jim', 'role': 'manager', 'salary': 85000.0}]
