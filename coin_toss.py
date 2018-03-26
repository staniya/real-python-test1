from random import randint

flips = 0
trials = 10000
'''
heads = 0
tails = 1
'''

for trial in range(0, trials + 1):
    flips += 1
    if randint(0,1) == 0:
        while randint(0, 1) == 0:
            flips += 1
        flips += 1           
    elif randint(0,1) == 1:
        while randint(0, 1) == 1:
            flips += 1
        flips += 1
        
print(f"The average number of flips was {flips / trials}")



                
            
        
