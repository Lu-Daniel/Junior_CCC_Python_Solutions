#J2_ShiftySum
#2018

N = input()
k = int(input())
totalSum = int(N)

for i in range(k):
    print(totalSum)
    N += "0"
    totalSum += int(N)
    

print(totalSum)