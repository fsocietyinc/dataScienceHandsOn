# Author: Prasad Chavan 19UME305
# Write a python program to print 'n' terms of
# Fibonacci series using iteration.

maxTerms = int(input("Enter the desired number of fibonacci sequence: ")) 

# First two terms of fibonacci sequence are predetermined.
numOne, numTwo = 0, 1
count = 0

# Check if the number of terms is valid i.e the nuumber of terms is positive.
if maxTerms <= 0:
   print("Please enter a positive integer")
elif maxTerms == 1:
   print("Fibonacci sequence upto",maxTerms,":")
   print(numOne)
else:
   print("Fibonacci sequence:")
   while count < maxTerms:
      print(numOne)
      nth = numOne + numTwo
      # Update values such that latest number is numTwo and the preceding number is numOne.
      numOne = numTwo
      numTwo = nth
      count += 1