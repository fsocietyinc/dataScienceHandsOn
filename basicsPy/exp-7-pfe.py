# Author: Prasad Chavan 19UME305
# Write a python program to demonstrate constructors.

# Creating new class
class student:
    
    # Define constructor. # __init__ is known as the constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def check_fail_pass(self):
        if self.marks >= 40:
            return True
        else:
            return False

# Creating new objects
st1 = student("Akshay", 95)
st2 = student("Ajit", 75)
st3 = student("Amar", 39)
st4 = student("Aditya", 00)

is_pass=st1.check_fail_pass() 
print("name=",st1.name ,", marks=",st1.marks ,"passed=", is_pass)
is_pass=st2.check_fail_pass()
print("name=",st2.name ,", marks=",st2.marks,"passed=" ,is_pass)
is_pass=st3.check_fail_pass()
print("name=",st3.name ,", marks=",st3.marks,"passed=", is_pass)
is_pass=st4.check_fail_pass()
print("name=",st4.name ,", marks=",st4.marks,"passed=", is_pass)


# Updating object attribute
st3.marks= 42

is_pass = st3.check_fail_pass()
print("name=",st3.name ,",Rechecking marks=",st3.marks,"passed=", is_pass)

# Deleting object
del st4