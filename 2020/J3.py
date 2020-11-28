#2020
#J3_Art

N = int(input("Enter the number of drops: "))
x_list = []
y_list = []

for i in range(N):
    coordinate = input("Enter the coordinate in (x, y): ")
    comma = coordinate.find(",")
    x_val = coordinate[:comma]
    x_list.append(int(x_val))
    x_list.sort()
    y_val = coordinate[comma+2:]
    y_list.append(int(y_val))
    y_list.sort()

x1 = str(x_list[0] - 1)
x2 = str(x_list[N-1] +1)
y1 = str(y_list[0] - 1)
y2 = str(y_list[N-1] + 1)

print(x1+", "+y1)
print(x2+", "+y2)


