colors = ["red", "green", "burnt sienna", "blue"]
scores = [10, 8, 9, -2, 3]
my_list = ["one", 2, 3.0]

print(colors[3])
print(my_list[0:2])

animals = []
animals.append("lion")
animals.append("tiger")
animals.append("cheetah")
animals.append("jaguar")
print(animals)

animals.remove("tiger")
animals.remove("lion")
print(animals)


cities = []
cities.extend(["San Francisco", "Boston", "New York", "Los Angeles", "Chicago"])
print(cities)


print(colors.index("burnt sienna"))

#You can't assign a string name to replace a string that already exists because
#both names will just point to the same object

animals = ["lion", "tiger", "frumious Bandersnatch"]
large_cats = animals[:]
large_cats.append("leopard")
print(large_cats)
print(animals)

#You can achieve the same results by using the extend() method
animals = ["lion", "tiger", "frumious Bandersnatch"]
large_cats = []
large_cats.extend(animals)
print(large_cats)

# do not reassign the list to itself like this: animals = animals.append("jubjub")

animals.sort()
print(animals)


two_by_two = [[1,2], [3,4]]
#assigning a list inside of another list
print(two_by_two[1][0])

groceries = "eggs, spam, pop rocks, cheese"
grocery_list = groceries.split(", ")
print(grocery_list)

desserts = ["ice cream", "cookies"]
desserts.sort()
print(desserts)
print(desserts.index("ice cream"))

food = []
food.extend(desserts)
print(food)

food.append("broccoli")
food.append("turnips")
print(food)
print(desserts)

food.remove("cookies")
print(food)
print(food[0:2])

cookies = "cookies, cookies, cookies"
breakfast = cookies.split(",")
print(breakfast)

def function(x):
    for num in x:
        if num >= 1 and num <= 20:
            print(num)

list = [2, 4, 8, 16, 32, 64]
list.sort()
print(function(list))


def enrollment_stats(list_of_universities):

    student_enrollment_values = []
    student_tuition = []

    for universities in list_of_universities:
        student_enrollment_values.append(universities[1])
        student_tuition.append(universities[2])

    return student_enrollment_values, student_tuition

def mean(my_list):
    if len(my_list) == 0:
        print("There is no value within this list")
    list_sum = 0
    for i in range(len(my_list)):
        list_sum += float(my_list[i])
    return int(list_sum / len(my_list))

def median(my_list):
    sorts = sorted(my_list)
    length = len(sorts)
    if not length % 2:
        return (sorts[int(length / 2)] + sorts[int(length / 2 - 1)]) / 2.0
    return sorts[int(length / 2)]

if __name__ == '__main__':

    university = [
        ['California Institute of Technology', 2175, 37704],
        ['Harvard', 19627, 39849],
        ['Massachusetts Institute of Technology', 10566, 40732],
        ['Princeton', 7802, 37000],
        ['Rice', 5879, 35551],
        ['Stanford', 19535, 40569],
        ['Yale', 11701, 40500],
    ]
print(university)               
total = enrollment_stats(university)

print(total[0])
print("\n")

print("*****" * 5)
print(f"Total students:  {sum(total[0])}")
print(f"Total tuition:  ${sum(total[1])}")
print(f"\nStudent mean:  {mean(total[0])}")
print(f"Student median:  {median(total[0])}")
print(f"\nTuition mean:  ${mean(total[1])}")
print(f"Tuition median:  ${median(total[1])}")
print("*****" * 5)

print("\n")
                
                

'''   
    student_mean = sum(studnet_enrollment_values)/

        
    for (user_input, user_input2, user_input3) in x:
        user_input = input("Which university are you attending? ")
        user_input2 = input("How many students are enrolled there? ")
        user_input3 = input("What is the annual tuition fee? ")
        if (user_input, user_input2, user_input3) == None:
            print("You did not enter enough information")
            break
        university = (user_input1, user_input2, user_input3)
        list_two = university.split()
        print(list_two)
        
universities = []
universities.append(list_two)
universities.sort()
print(enrollment_stats(universities))
'''
        
    
    






































