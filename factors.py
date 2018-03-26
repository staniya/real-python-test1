user_input = int(input("Enter a positive integer: "))

for x in range (1, user_input + 1):
    if (user_input % x) == 0:
        print (f"{x} is a divisor of {user_input}")

for i in range(0, 4):
    if i == 2:
        break
    print(i)

print("Finished with i= ", str(i))

for i in range(0, 4):
    if i == 2:
        continue
    print(i)

print("Finished with i= ", str(i))


phrase = "it marks the spot"

for letter in phrase:
    if letter == "X":
        break
else:
    print("There was no 'X' in the phrase")

tries = 0
while tries < 3:
    password = input("Password:")
    if password == "I<3KendrickLamar":
        break
    else:
        tries += 1
else:
    print("Suspicious activity. The authorities have been alerted.")


while True:
    repeated_input = input("Enter something: ")
    if repeated_input == ("q" or "Q"):
        print("sucess")
        break

for i in range (1, 51):
    if i%3 == 0:
        continue
    else:
        print(i)

def divide(num1, num2):

    try:
        print(num1 / num2)
    except (TypeError, ZeroDivisionError):
        print("encountered a problem")

try:
    number = int(input("Enter an non-zero integer: "))
    print(f"10/{number} = {10.0/number}")
except ValueError:
    print("You did not enter an integer.")
except ZeroDivisionError:
    print("You cannot enter 0.")

'''
try:
    #dumbshit that would cause the code to break
except:
    print("You did it! You screwed things up")
'''

while True:
    try:
        number =input("Input an integer: ")
        print(int(number))
        break
    except ValueError:
        print("try again")

from random import randint
print(randint(0,100))

    
    

    
