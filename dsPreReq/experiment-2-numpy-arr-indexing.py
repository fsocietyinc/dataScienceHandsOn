# Author: Prasad Chavan 19UME305
# Experiment 2: Implementation of array processing using NumPy.

import numpy as np # import numpy and name it np

# slice items between indexes
a = np.arange(10)
print (a[2:5]) # prints [2 3 4]
# slice items starting from index
a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print (a[1:] ) # prints [[3 4 5][4 5 6]]

# Slicing can also include ellipsis (…) to make a selection tuple of the same length as the
# dimension of an array. If ellipsis is used at the row position, it will return an ndarray comprising
# of items in rows.

a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print (a[...,1]) # this returns array of items in the second column
print (a[1,...]) # this returns array of all items from the second row
print (a[...,1:]) # this returns array of all items from column 1 onwards

# Integer Indexing: selecting any arbitrary item in an array based on its Ndimensional index
x = np.array([[1, 2], [3, 4], [5, 6]])
y = x[[0,1,2], [0,1,0]] # includes elements at (0,0), (1,1) and (2,0) from the first array
print (y) # [1 4 5]

# Boolean Indexing: 
x = np.array([[ 0, 1, 2],[ 3, 4, 5],[ 6, 7, 8],[ 9, 10, 11]])
print (x[x > 5]) # prints [ 6 7 8 9 10 11]