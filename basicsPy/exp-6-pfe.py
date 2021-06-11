# Author: Prasad Chavan 19UME305
# Write a Python program to demonstrate working
# of classes and objects

class Department:
    "This is a department class"
    name = "Mechanical"

    def greet(self):
        print(f'Hello! Welcome to {self.name} Engineering department.')


# create a new object of department class
student = Department()

# Output: "This is a department class"
print(Department.__doc__)

# Print attribuite name from class department.
print(student.name)

# Output: <function Department.greet>
print(Department.greet)

# Output: <bound method Department.greet of <__main__.Department object>>
print(student.greet)

# Calling object's greet() method
# Output: Hello! Welcome to Mechanical Engineering department.
student.greet()