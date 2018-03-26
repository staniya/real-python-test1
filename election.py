from random import randint

candidate_a = 0
candidate_b = 0
total_a_wins = 0
total_b_wins = 0
trials = 10000
for trial in range(0, trials + 1):
    if randint(0, 1) == 0:
        candidate_a +=1
    else:
        candidate_b += 1

        if candidate_a > candidate_b:
            total_a_wins += 1
        else:
            total_b_wins += 1
region1 = ((0.87 * candidate_a)/ ((0.87 * candidate_a) + (0.13 * candidate_b)))
print(f"In region 1, candidate A has a {region1 * 100}% chance of winning")

for trial in range(1, trials + 1):
    if randint(0, 1) == 0:
        candidate_a +=1
    else:
        candidate_b += 1

        if candidate_a > candidate_b:
            total_a_wins += 1
        else:
            total_b_wins += 1
region2 = ((0.65 * candidate_a)/ ((0.65 * candidate_a) + (0.35 * candidate_b)))
print(f"In region 2, candidate A has a {region2 * 100}% chance of winning")

for trial3 in range(1, trials + 1):
    if randint(0, 1) == 0:
        candidate_a +=1
    else:
        candidate_b += 1

        if candidate_a > candidate_b:
            total_a_wins += 1
        else:
            total_b_wins += 1
region3 = ((0.17 * candidate_a)/ ((0.83 * candidate_a) + (0.17 * candidate_b)))
print(f"In region 3, candidate A has a {region3 * 100}% chance of winning")


print(f"The probability that Candidate A will win is {(region_total/3) * 100}%")
print(f"The probability that Candidate B will win is {100 - ((region_total/3) * 100)}%")
