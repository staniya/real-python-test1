def celsius_to_farenheit(c):
    '''converting celsius to farenheit'''
    f = (c * 9/5) + 32
    return f

def farenheit_to_celsius(f):
    '''converting farenheit to celsius'''
    c = (f-32) * 5/9
    return c

c = 37
print(f"{c} degrees C = {celsius_to_farenheit(c)} degrees F")

f = 72
print(f"{f} degrees F = {farenheit_to_celsius(f)} degrees C")

n = 1
while (n<5):
    print("n=", n)
    n = n + 1
print("Loop finished")

for n in range(0, 3):
    print("n=", n)
print("Loop finished")

for n in range(1,4):
    for j in ["a","b","c"]:
        print("n=", n, "and j =", j)

for n in range(2,10):
    print("n =", n)

n = 2
while (n<11):
    n = n + 1
    print("n=", n)

def doubles(num):
    return num * 2

my_num = 2
for i in range(0, 3):
    my_num = doubles(my_num)
    print(my_num)

