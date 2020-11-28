#2020
#J1_Dog_Treats

S = int(input("Enter number of small treats: "))
M = int(input("Enter the number of medium treats: "))
L = int(input("Enter the number of large treats: "))

score = ((1*S)+(2*M)+(3*L))
if score >= 10:
    print("happy")
else:
    print("sad")

