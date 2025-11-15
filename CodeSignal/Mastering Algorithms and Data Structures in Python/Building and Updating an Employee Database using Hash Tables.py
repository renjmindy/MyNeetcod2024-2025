from collections import defaultdict

# TODO: Create a Python dictionary to serve as a hash table
mp = defaultdict()
# TODO: Add employee names with their roles to the dictionary
mp['Alex'] = 'Software Engineer Lead'
mp['Adam'] = 'DevOps Lead'
mp['Darryl'] = 'Head of Research and Development'

# TODO: Print the initial employee database
print("Before updating...")
for k, v in mp.items():
    print(f"name: {k}, role: {v}")

# TODO: Update the role of an employee in the database
mp['Darryl'] = 'CTO: Chief of Technology Officer'

# TODO: Print the database after the employee role update
print("\nAfter updating Darryl's job title...")
for k, v in mp.items():
    print(f"name: {k}, role: {v}")
    
# TODO: Remove an employee from the database
del mp['Darryl']

# TODO: Print the final employee database after the removal
print("\nAfter Darryl job hopping...")
for k, v in mp.items():
    print(f"name: {k}, role: {v}")
