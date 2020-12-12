#2018
#J2_Occupy_Parking

N = int(input())

str1 = input()
str2 = input()
counter = 0

for i in range (N):
    if str1[i] == "C":
        if str1[i] == str2[i]:
            counter += 1
print(counter)