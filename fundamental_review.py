print("\n")

zero = 0
one = 23
two = [5, 4, 3, 2, 1]
three = ("I", "love", "Python!")
four = [["P", "y", "t", "h", "o", "n"],["i", "s"],["h", "a", "r", "d"]]
five = {"happy":"birthday", "fish":"chips", "shinn": "great"}
six = {1, 2, 3, 4, 5, 6, 8, 9, 10}
days = ("Fri", "Sat", "Wed")
x, y, seven = days

print(f"zero:  {zero == 0}")
print(f"one:   {one > 22}")
print(f"two:   {len(two) == 5}")
print(f"three: {three[2] == 'Python!'}")
print(f"four:  {four[0][5] == 'n' and four[0][0] == 'P' and four[2][1] == 'a'}")
print(f"five:  {five.get('fish') == 'chips'}")
print(f"five:  {len(five) == 3}")
print(f"six:   {len(six & {2,5,7}) == 2}")
print(f"seven: {seven == 'Wed'}")

print("\n")


# Find a value for the `value` variable
# so that all print statements return True.

value = [1, 1, 1, 1]

# DO NOT CHANGE ANYTHING BELOW THIS LINE #
# ------------------------------------ #

if type(value) is list:
    print(True)
else:
    print(False)

for x in value:
    if not type(x) is int:
        print(False)
    else:
        print(True)

num = 0
while num < value[2]:
    print(True)
    num += 1

for y in range(value[3]):
    if y in value:
        print(False)

try:
    value[5] = "Cat"
    while True:
        print(False)
except IndexError:
    print(True)

try:
    assert value[3] == -1
except AssertionError:
    print(True)

# -------------------------------------- #

