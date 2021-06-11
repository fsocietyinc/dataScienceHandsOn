# Author: Prasad Chavan 19UME305
# Experiment 2: Implementation of array processing using NumPy.

import numpy as np # import numpy and name it np

a = np.array([1, 2, 3])
# Create a rank 1 array
print(type(a))
# Prints "<class 'numpy.ndarray'>"
print(a.shape)
# Prints "(3,)"
print(a[0], a[1], a[2])
# Prints "1 2 3"
a[0] = 5
# Change an element of the array
print(a)
# Prints "[5, 2, 3]"
b = np.array([[1,2,3],[4,5,6]])
# Create a rank 2 array
print(b.shape)
# Prints "(2, 3)"
print(b[0, 0], b[0, 1], b[1, 0])
# Prints "1 2 4"

# Numpy also provides many functions to create arrays:
a = np.zeros((2,2))
# Create an array of all zeros
print(a)
# Prints "[[ 0. 0.][0. 0.]]"
b = np.ones((1,2))
# Create an array of all ones
print(b)
# Prints "[[ 1. 1.]]"
c = np.full((2,2), 7)
# Create a constant array

print(c)
# Prints "[[ 7. 7.][ 7. 7.]]"
d = np.eye(2)
# Create a 2x2 identity matrix
print(d)
# Prints "[[ 1. 0.][ 0. 1.]]"
e = np.random.random((2,2))
# Create an array with random values
print(e)
# Might print "[[0.91940167 0.08143941][0.68744134 0.87236687]]"
# Creating an array from sub-classes:
np.array(np.mat('1 2; 3 4')) # Creates array([[1, 2],[3, 4]])
np.array(np.mat('1 2; 3 4'), subok=True) # Creates matrix([[1, 2],[3, 4]])