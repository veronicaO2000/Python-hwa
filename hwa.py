#!/usr/bin/python3

# Class:     CSCI 656
# Program:   Assignment A
# Author:    Veronica Olvera
# Z-number:  z1845587
# Date Due:  02/09/22

# Purpose:   Decrement from a given number by 1 and increase the increment when the current number ends in 0.
#            Continue until the subtration causes the current number to go negative.

# Execution: python3 hwa.py

import sys

if len(sys.argv) == 2:                      # Check if an argument was given
    if not sys.argv[1].isdigit():           # Check if the argument is numeric
        print("Argument is not a positive integer")
        print()
        exit()
    startingNum = sys.argv[1]               # Set the starting number to the number given - the second command line argument    
else:
    startingNum = 1000                      # Otherwise, default to 1000

currentNum = int(startingNum)

print(" decrement\t current\tcount\n\t%16d" % currentNum)

decrementBy = 1
count = 0
numCount = 0
numPassed  = 0

while True:
    currentNum -= decrementBy                   # Subtract from the current number by the current increment
    numPassed += decrementBy                    # Increment the numbers passed by the the current increment

    if currentNum < 0:
        currentNum += decrementBy               
        numPassed -= decrementBy                
        print("%10d%14d%13d   " % (decrementBy, currentNum, count), '*' * count)
        break

    count += 1                                  # Increment the current count

    if currentNum == 0:
        print("%10d%14d%13d   " % (decrementBy, currentNum, count), '*' * count)
        break  

    if currentNum % 10 == 0:                    # Check if the current number ends in 0
        print("%10d%14d%13d   " % (decrementBy, currentNum, count), '*' * count)
        decrementBy += 1                        # Increase the Increment
        numCount += count                       # Increment the numbers spoken by the current count
        count = 0                               # Set the count back to 0

numCount += count

avgCycleIncr = numCount / decrementBy           # Calculate the average cycle per increment
avgNumIncr = numPassed / decrementBy            # Calculate the numbers per increment

print("\nThere were", numCount, "numbers spoken with", decrementBy, 
    "different increments. Average cycles/incr = {:.2f}".format(avgCycleIncr))

print("\nThere were", numPassed, "numbers passed by with", decrementBy,
    "different increments. Average numbers/incr = {:.2f}".format(avgNumIncr))