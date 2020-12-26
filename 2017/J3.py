#J2_Exactly_Electrical
#2017

A = input()
B = input()
t = int(input())

car_coords = 0
destination_coords = 0

space = A.find(" ")
a = int(A[:space])
c = int(A[space+1:])
car_coords += a
car_coords += c
spcae = B.find(" ")
b = int(B[:space])
d = int(B[space+1])
destination_coords += b
destination_coords += d

value = abs(destination_coords - car_coords)

if (t - value) % 2 == 0:
    print("Y")
else:
    print("N")