#2019
#J2_Time_to_Decompress

L = int(input())
myList = []
for i in range (L):
    N = input()
    space = N.find(" ")
    number = int(N[:space])
    characters = N[space+1:]
    myList.append(characters*number)

for i in range (L):
    print(myList[i])