#2020
#J2_Epidemiology

P = int(input(""))
N = int(input(""))
R = int(input(""))

day = 0
peopleInfected = N
totalInfected = N
while totalInfected <= P:
    peopleInfected *= R
    day += 1
    totalInfected += peopleInfected
print(day)
