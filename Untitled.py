from random import random, randint

def dice_toss():
    trials = 0
    total = 0
    while (trials <= 10000):
        trials += 1
        total += randint(1,6)
    average = total/trials
    print(average)

dice_toss()




def election():
    trials = 10000
    total_a = 0
    total_b = 0
    for trial in range(0, trials + 1):
        candidate_a = 0
        candidate_b = 0
        if random() < 0.87:
            candidate_a += 1
        else:
            candidate_b += 1
        if random() < 0.65:
            candidate_a += 1
        else:
            candidate_b += 1
        if random() < 0.17:
            candidate_a += 1
        else:
            candidate_b += 1
        if candidate_a > candidate_b:
            total_a += 1
        else:
            total_b += 1
    print(f"The probability that candidate A will win is {(total_a/trials) * 100}%")
    print(f"The probability that candidate B will win is {(total_b/trials) * 100}%")

election()

def enrollment_stats(list_of_universities):
    enrolled_students = []
    tuition_fees = []
    for university in list_of_universities:
        enrolled_students.append(university[1])
        tuition_fees.append(university[2])
    return(enrolled_students, tuition_fees)

def mean(my_list):
    total = 0
    for i in range(len(my_list)):
        total += float(my_list[i])
    average = float(total/len(my_list))
    return(average)

def median(my_list):
    sorts = sorted(my_list)
    length = len(sorts)
    if not length % 2:
        return (sorts[int(length / 2)] + sorts[int(length / 2 - 1)]) / 2.0
    middle = sorts[int(length/2)]
    return(middle)

if __name__ == '__main__':
    universities = [
        ['California Institute of Technology', 2175, 37704],
        ['Harvard', 19627, 39849],
        ['Massachusetts Institute of Technology', 10566, 40732],
        ['Princeton', 7802, 37000],
        ['Rice', 5879, 35551],
        ['Stanford', 19535, 40569],
        ['Yale', 11701, 40500]
    ]
totals = enrollment_stats(universities)
print(totals[0])

print("\n")
print("*****" * 5)
print(f"Total students:  {sum(totals[0])}")
print(f"Total tuition:  ${sum(totals[1])}")
print(f"\nStudent mean: {mean(totals[0])}")
print(f"Student median: {median(totals[0])}")
print(f"\nTuition mean: ${mean(totals[1])}")
print(f"Tuition median: ${median(totals[1])}")
print("*****" * 5)
print("\n")



def cats_with_hats_class(cats_array):
    cats_with_hats = []
    for num in range (1, 101):
            for cat in range(1, 101):
                if cat % num == 0:
                    if cats_array[cat] is True:
                        cats_array[cat] = False
                    else:
                        cats_array[cat] = True
    for cat in range(1, 101):
        if cats[cat] is True:
            cats_with_hats.append(cat)
    return cats_with_hats

cats = [False] * (101)
print(f"cats #{cats_with_hats_class(cats)} have hats")





number_of_cats = 100
cats_with_hats = []
number_of_laps = 100

for lap in range (1, number_of_laps + 1):
    for cat in range (1, number_of_laps +1):
        if cat%lap == 0:
            if cat in cats_with_hats:
                cats_with_hats.remove(cat)
            else:
                cats_with_hats.append(cat)
print(cats_with_hats)






allCats = {}

for i in range(1, 101):
    allCats[i] = False
for i in range(1, 101):
    for cats, hats, in allCats.items():
        if cats % i == 0:
            if allCats[cats]:
                allCats[cats] = False
            else:
                allCats[cats] = True
for cats, hats in allCats.items():
    if allCats[cats]:
        print(f"Cat {cats} has a hat.")
    else:
        print(f"Cat {cats} is hatless.")



import os
import csv

my_path = "/Users/staniya/Downloads/book1-exercises-master/chp09/practice_files"
dictionary = {}

with open(os.path.join(my_path, "scores.csv"), "r") as my_input:
    csv_read = csv.reader(my_input)
    
    for users, scores in csv_read:
        scores = int(scores)
        if users in dictionary:
            if scores > dictionary[users]:
                dictionary[users] = scores
        else:
            dictionary[users] = scores

for users in sorted(dictionary):
    print(users, dictionary[users])
    









