# Author: Prasad Chavan 19UME305
# Write a python program to demonstrate tuples and
# lists using python.

# Lists in python

# A list
egList = [1, 2, 3, 4, 5]

info = [1, 2, 3, 'dkte', 'prasad', 'omraj']

# indexed Out: 1
print(info[0])

# sliced Out: [​'dkte'​, ​'prasad'​, ​'omraj'​]
print(info[-3:])

# Out: [​1​, ​2​, ​3​, ​'dkte'​, ​'prasad'​, ​'omraj'​]
print(egList[:])

# concatenation Out: [​5​, ​6​, ​7​, ​1​, ​2​, ​3​, ​'dkte'​, ​'prasad'​, ​'omraj'​]
cnct_info = [5, 6, 4] + info
print(cnct_info)

# mutable
info[3] = 64
print(info[3])  # Out: 64

# use of append()
info.append('ds minor')
print(info) # [1, 2, 3, 64, 'prasad', 'omraj', 'ds minor']
