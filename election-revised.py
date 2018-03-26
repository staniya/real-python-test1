from random import random

total_candidate_a = 0
total_candidate_b = 0
trials = 10000

for trial in range(0, trials + 1):
    try:
        candidate_a = 0
        candidate_b = 0
        #random() generates a random number between (0.0, 1.0)
        if random() < 0.87:
            candidate_a += 1
        else:
            candidate_b += 1
        #this is for region1
        if random() < 0.65:
            candidate_a += 1
        else:
            candidate_b += 1
        #this is for region2
        if random() < 0.17:
            candidate_a += 1
        else:
            candidate_b += 1
        #this is for region3
        if candidate_a > candidate_b:
            total_candidate_a += 1
        else:
            total_candidate_b += 1
            
    except(ValueError, ZeroDivisionError, TypeError):
         print("try again")
         continue


print(f"The probability that Candidate A will win is {(total_candidate_a / trials) * 100}%")
print(f"The probability that Candidate B will win is {(total_candidate_b / trials) * 100}%")

        
            
        
        
