trials = 0
trials_total = 100

def number_of_hats(hats):
    for trials in range(1, trials_total + 1):
        trials += 1
        hats = 100 * (1/trials)
        print(hats)

def cats_class():
    cats_with_hats = []
    number_of_cats = 100
    for trial in range(1, trials_total + 1):
        for cat in range(1, number_of_cats + 1):
            if cat % trial == 0:
                if cat in cats_with_hats:
                    cats_with_hats.remove(cat)
                else:
                    cats_with_hats.append(cat)
    print(cats_with_hats)

cats_class()


theCats = {}

for trial in range(1, 101):
    theCats[trial] = False

for trial in range(1, 101):
    for cats, hats in theCats.items():
        if cats % trial == 0:
            if theCats[cats]:
                theCats[cats] = False
            else:
                theCats[cats] = True

for cats, hats in theCats.items():
    if theCats[cats]:
        print(f"Cat {cats} has a hat.")
    else:
        print(f"Cat {cats} is hatless!")
