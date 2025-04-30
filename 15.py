weight = int(input("Enter your weight:"))
checker = input("(l) for lbs or (k) for kg:")
if checker == 'l':
    converted = round(weight * 0.45)
    print(f'Your weight in kg is {converted}')
else:
    converted = round(weight / 0.45)
    print(f'Your weight in lbs is {converted}')