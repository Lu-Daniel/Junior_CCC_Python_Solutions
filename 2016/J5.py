#J5_Tandem_Bicycle
#2016

question = int(input())
N = int(input())
D = input()
P = input()

D = D.split(" ")
P = P.split(" ")
D_list = []
P_list = []
for i in range(N):
    D_list.append(int(D[i]))
    P_list.append(int(P[i]))
D_list.sort()
P_list.sort()

sum = 0

if question == 1:
    for i in range(N):
        sum += max(D_list[i], P_list[i])
else:
    for i in range(N):
        sum += max(D_list[i], P_list[N-i-1])
print(sum)