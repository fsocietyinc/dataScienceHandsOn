# List
# Author: Prasad Chavan 19UME305


#creating 3 lists
list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5 ];
list3 = ["a", "b", "c", "d"];

#Accesing values
print ("list1[0]: ", list1[0])

#slicing
print ("list2[1:]: ", list2[1:])
print("list3[:-2]", list3[:-2])

#Updating values
list2[2] = 6
print ("list2[1:]: ", list2[1:])

#deleting list
del list1[0:]
print("list1[0:]", list1[0:])

#basic list operations
print(len(list2))

# Concatenation
print((1, 2, 3) + (4, 5, 6))

#Repeat
print(('Hi!',) * 4)

#tuple membership test
print(6 in list2)

#iteration
for x in (1,2,3,4,5) : print (x, end = ' ')