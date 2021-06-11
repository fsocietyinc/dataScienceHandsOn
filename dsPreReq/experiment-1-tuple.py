# Tuple
# Author: Prasad Chavan 19UME305

#creating tuples
tuple1 = ('physics', 'chemistry', 1997, 2000)
tuple2 = (1, 2, 3, 4, 5 )
tuple3 = "a", "b", "c", "d"
tuple4 = ();
tuple5 = (50,)

#Accesing tuple
print ("tuple1[0]: ", tuple1[0])

#slicing
print ("tuple2[1:]: ", tuple2[1:])
print ("tuple3[:-2]", tuple3[:-2])

#delete 
del tuple1


#basic operations
print(len(tuple5))


# Concatenation
print((1, 2, 3) + (4, 5, 6))

#Repeat
print(('Hi!',) * 4)

#tuple membership test
print(3 in tuple2)

#iteration
for x in (1,2,3) : print (x, end = ' ')