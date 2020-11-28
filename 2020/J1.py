#2020
#J2_Epidemiology

P = int(input(""))
N = int(input(""))
R = int(input(""))

day = 0
peopleInfected = N
while True:
    if peopleInfected > P:
        print(peopleInfected)
        break
    day += 1
    peopleInfected += peopleInfected*R


