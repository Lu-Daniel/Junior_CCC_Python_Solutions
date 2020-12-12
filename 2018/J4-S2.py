#2018
#J4/S2_Sunflowers

N = int(input())
sortedList = []
notSortedList = []

for i in range(N):
    flowers = input()
    flowers = flowers.split(" ")
    for i in range(N):
        sortedList.append(flowers[i])
for i in range(N**2):
    notSortedList.append(sortedList[i])

sortedList.sort()
smallestNumber = sortedList[0]

if notSortedList.index(smallestNumber) + 1 == 1:
    count = 0
    for i in range(N):
        for i in range(N):
            print(notSortedList[count], end = " ")
            count += 1
        print()
elif notSortedList.index(smallestNumber) + 1 == N:
    for i in range(N):
        for k in range(N):
            print(notSortedList[N-i-1+N*k], end = " ")
        print()
elif notSortedList.index(smallestNumber) + 1 == N**2:
    count = 0
    for i in range(N):
        for k in range(N):
            print(notSortedList[N**2-1-count], end = " ")
            count += 1
        print()
else:
    for i in range(N):
        count = 0
        for k in range(N):
            count += 3
            print(notSortedList[N**2-count+i], end = " ")
        print()