temperature = 30

if temperature > 30:                    #  >  <  ==  !=
    print("It's a hot day")
else:
    print("It's not a hot day")


#########################################

name_cha = len(input("Enter your name: "))
if name_cha < 3:
    print(f'Error your name has {name_cha} characters')
elif name_cha > 50:
    print(f'Error your name has {name_cha} characters')
else:
    print(f'Success!! your name has {name_cha} characters')