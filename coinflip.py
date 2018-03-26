from random import randint
heads = 0
tails = 0

for trials in range(0, 10000):
    while randint(0, 1) == 0:
        tails = tails + 1
    heads = heads + 1

print("heads/tails = ", heads/tails)


print(randint(1,6))

total = 0
trials = 10000
for trial in range(0, trials + 1):
    total = total + randint(1,6)
print(f"The average number resulting is: {total/trials}")
