from numpy import *
from random import random

question = int(input("Enter a positive integer: "))

for i in range(1, question + 1):
    try:
        if question%i == 0:
            print("{0} is a divisor of {1}".format(i, question))

    except ValueError:
        print("You did not enter a valid number")


# ------------------------------------------------------------------------------------

trials = 10000
total_candidate_a = 0
total_candidate_b = 0


for trial in range(0, trials + 1):
    try:
        candidate_a = 0
        candidate_b = 0

        value = random()
        if value < 0.87:
            candidate_a += 1
        else:
            candidate_b += 1
        if value < 0.65:
            candidate_a += 1
        else:
            candidate_b += 1
        if value < 0.17:
            candidate_a += 1
        else:
            candidate_b += 1

        if candidate_a > candidate_b:
            total_candidate_a += 1
        else:
            total_candidate_b += 1
    except ZeroDivisionError or ValueError:
        print("invalid values")

print("The chance of Candidate A wining is {0}%".format((total_candidate_a/trials)*100))
print("The chance of Candidate B wining is {0}%".format((total_candidate_b/trials)*100))