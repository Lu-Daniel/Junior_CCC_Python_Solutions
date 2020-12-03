#2019
#J3_Cold_Compress

N = int(input())
listEncoding = []
for i in range(N):
    encoding = input()
    listEncoding.append(encoding)
for i in range(N):
    output = ""
    count = 1
    for k in range(1, len(listEncoding[i])):
        if listEncoding[i][k-1] == listEncoding[i][k]:
            count += 1
        else:
            output += str(count) + " " + listEncoding[i][k-1] + " "
            count = 1   
    output += str(count) + " " + listEncoding[i][k] + " "
    count = 1              
    print(output)