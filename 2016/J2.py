#J2_Magic_Squares
#2016

myList = []
for i in range(4):
    line = input()
    line = line.split(" ")
    for i in range(4):
        myList.append(int(line[i]))

sum = myList[0] + myList[1] + myList[2] + myList[3]
for i in range(1, 4):
    newSum = 0
    for k in range(4):
        newSum += myList[k+4*i]
    if newSum != sum:
        output = "not magic"
        break
if output != "not magic":
    for i in range(4):
        newSum = 0
        for k in range(4):
            newSum += myList[k*4+i]
        if newSum != sum:
            output = "not magic"
            break
        else:
            output = "magic"
print(output)
