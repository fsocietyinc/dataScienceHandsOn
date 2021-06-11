# Author: Prasad Chavan 19UME305
# Write a python program using function to find all
# prime numbers within a given range.

def primeRange(lowerN, upperN):
    
    print(f"Prime numbers betwee {lowerN} and {upperN} are:")

    for num in range(lowerN, upperN + 1):
    # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num, end = " ")

lower = int(input("Enter lower range:"))
upper = int(input("Enter upper range:"))

primeRange(lower, upper)